from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.urls import reverse
from .models import JornadaH, Carrera, DetallesCarrera, ActualizarEstatusCarrerasCorriendo, ActualizarEstatusCarrerasCorriendoPendientes
from .forms import (IncluirCarreraForm, IncluirJornadaForm, ActualizarJornadaForm, RegistrarDetallesForm, 
					ActualizarDetallesForm, ActualizarCarreraForm, FinalizarCarreraForm, ListaCarreraForm,
                    FinalizarDetallesForm, RegistrarResultadosForm)
from django.views.generic.list import ListView
from flyhorse.mixin import AuthenticatedEncarMixin
from datetime import datetime
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apps.apuesta.models import Apuesta, TipoApuesta, DetalleApuesta
from apps.monedavirtual.models import Transaccion
from apps.usuario.models import User

# Create your views here.
"""
APS para gestionar el cambio automático de estado de las carreras
"""
#Necesito garantizar de alguna manera que este código se ejecute cada vez que se encienda el server.
#Por eso está acá afuera, sin ninguna función ni nada.
#Ahora, como el APS no ofrece persistencia de la data, tenemos que consultar en la BD los trabajos
#que están pendientes.
#Se guardan en la tabla Job. Tienen estatus, fecha, hora y un ID único.
#A partir de esto, y cada vez que se ejecuta el server, se cargan a un scheduler único todos los
#trabajos pendientes, permitiendo añadir más si es necesario.
scheduler = BackgroundScheduler() #Declaro el scheduler
tz = timezone('America/Caracas') #Zona horaria porque el APS se vuelve un despelote sin eso
jobs = Carrera.objects.filter(id_jh__fecha__gte=datetime.now(tz).date(),hora__gte=datetime.now(tz).time(),estatus='a') #Consulto si hay trabajos que están pendientes en la BD
if jobs:
	for job in jobs:
		f = job.id_jh.fecha.strftime("%Y-%m-%d")
		h = job.hora.strftime("%H:%M:00")
		fh = f + ' ' + h
		scheduler.add_job(ActualizarEstatusCarrerasCorriendo,'date', run_date=fh, timezone='America/Caracas') #Los cargo al scheduler interno
jobs = Carrera.objects.filter(id_jh__fecha__lte=datetime.now(tz).date(),hora__lte=datetime.now(tz).time(),estatus='a') #Consulto si hay trabajos "vencidos" en la BD
if jobs:
	for job in jobs:
		ActualizarEstatusCarrerasCorriendoPendientes(job.id_jh.fecha, job.hora) #No los cargo: los actualizo de una vez
scheduler.print_jobs() #Imprimirlos, para confirmar que todo marcha bien.
#scheduler.start() #Inicio. Si no inicio no sirve de nada porque no habrá nadie esperando para ejecutar el método

"""
CARRERAS

"""

class IncluirCarrera(AuthenticatedEncarMixin, CreateView):
	model = Carrera
	form_class = IncluirCarreraForm
	template_name = "carrera/incluirC.html"

	def get_success_url(self):
		return reverse_lazy('detalleC', kwargs={'pk': self.object.pk, 'modal': 'show'})

#Es evidente que hay que crear el trabajo con el APS cada vez que se incluye una carrera.
#Por eso está la sobrecarga del form_valid. Este crea el trabajo tanto en BD como en el scheduler interno.
	def form_valid(self, form): 
		instance = form.save(commit=False)
		fecha = form.cleaned_data['id_jh'].fecha
		fecha = fecha.strftime("%Y-%m-%d")
		hora = form.cleaned_data['hora'].strftime("%H:%M:00")
		fh = fecha + ' ' + hora
		print(fh)
		trabajo = Job()
		trabajo.fecha = fecha
		trabajo.hora = hora
		trabajo.save()
		scheduler.add_job(ActualizarEstatusCarrerasCorriendo,'date', run_date=fh, timezone='America/Caracas')
		scheduler.print_jobs()
		return super().form_valid(form)	
		

class ListaCarrera(AuthenticatedEncarMixin, ListView):
	model = Carrera
	template_name = "carrera/listaCr.html"

	def get_context_data(self, **kwargs):
		est = self.kwargs.get('estatus')
		context = super(ListaCarrera, self).get_context_data(**kwargs)
		context["object_list"] = Carrera.objects.filter(id_jh__estatus='a')
		return context

class ActualizarCarrera(AuthenticatedEncarMixin, UpdateView):
	model = Carrera
	form_class = ActualizarCarreraForm
	template_name = "carrera/actualizarC.html"
	success_url = reverse_lazy('listaCr')

class FinalizarCarrera(AuthenticatedEncarMixin, UpdateView):
	model = Carrera
	form_class = FinalizarCarreraForm
	template_name = "carrera/finalizarC.html"
	success_url = reverse_lazy('listaCr')

class EliminarCarrera(AuthenticatedEncarMixin, UpdateView):
	model = Carrera
	form_class = FinalizarCarreraForm
	template_name = "carrera/eliminarC.html"
	success_url = reverse_lazy('listaCr')

"""
JORNADA
"""

class IncluirJornada(AuthenticatedEncarMixin, CreateView):
	model = JornadaH
	form_class = IncluirJornadaForm
	template_name = "jornada/incluirJ.html"

	def get_context_data(self, **kwargs):
		context = super(IncluirJornada, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context	

	def get_success_url(self):
		return reverse_lazy('incluirJh', kwargs={'modal': 'show'})

class ListaJornada(AuthenticatedEncarMixin, ListView):
	model = JornadaH
	template_name = "jornada/listaJ.html"

	def get_context_data(self, **kwargs):
		context = super(ListaJornada, self).get_context_data(**kwargs)
		context['jornadas'] = JornadaH.objects.filter(estatus='a')
		context['show'] = self.kwargs.get('modal')
		return context	

class ActualizarJornada(AuthenticatedEncarMixin, UpdateView):
	model = JornadaH
	form_class = ActualizarJornadaForm
	template_name = "jornada/actualizarJ.html"

	def get_success_url(self):
		return reverse_lazy('consJh', kwargs={'pk': self.object.id ,'modal': 'show'})



class EliminarJornada(AuthenticatedEncarMixin, DeleteView):
	model = JornadaH
	template_name = "jornada/eliminarJ.html"

	def get_success_url(self):
		return reverse_lazy('listaJh', kwargs={'modal': 'show'})

class ConsultarJornada(AuthenticatedEncarMixin, ListView):
	model = JornadaH
	second_model = Carrera
	template_name = "jornada/consultarJ.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ConsultarJornada, self).get_context_data(**kwargs)
		context['carreras'] = Carrera.objects.filter(id_jh = pk)
		context['jornadah'] = JornadaH.objects.get(id = pk)
		context['show'] = self.kwargs.get('modal')
		return context		


"""
DETALLES
"""
class ListaDetallesC(AuthenticatedEncarMixin, ListView):
	model = DetallesCarrera
	second_model = Carrera
	template_name = "carrera/listdetallesC.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ListaDetallesC, self).get_context_data(**kwargs)
		context['competidores'] = DetallesCarrera.objects.filter(id_carr=pk).order_by('numero', '-estatus')
		context['carrera'] = Carrera.objects.get(id=pk)
		context['show'] = self.kwargs.get('modal')
		return context
	
		
class RegistrarDetalles(AuthenticatedEncarMixin, CreateView):
	model = DetallesCarrera
	second_model = Carrera
	form_class = RegistrarDetallesForm
	template_name = "carrera/incluirD.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(RegistrarDetalles, self).get_context_data(**kwargs)
		context['carrera'] = Carrera.objects.get(id=pk)
		return context

	def get_success_url(self, **kwargs):
		pk = self.kwargs.get('pk')
		return reverse_lazy('detalleC', kwargs={'pk': pk,'modal':'show'})

class ActualizarDetalle(AuthenticatedEncarMixin, UpdateView):
	model = DetallesCarrera
	form_class = ActualizarDetallesForm
	template_name = 'carrera/actualizarD.html'
	
	def get_success_url(self):
		return reverse_lazy('detalleC', kwargs={'pk': self.object.id_carr.id,'modal':'show' })

class RetirarCompetidor(AuthenticatedEncarMixin, UpdateView):
	model = DetallesCarrera
	form_class = FinalizarDetallesForm
	template_name = 'carrera/eliminarD.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		context['DetallesCarrera'] = DetallesCarrera.objects.get(id=pk)
		return context

	def get_success_url(self):
		return reverse_lazy('detalleC', kwargs={'pk': self.object.id_carr.id, 'modal':'show'})

	def form_valid(self, form): 
		instance = form.save(commit=False)
		id_carr = instance.id_carr_id
		apuestas = Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=1) | Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=2) |Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=3) |Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=4) |Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=5) |Apuesta.objects.filter(id_carr_id=id_carr,tApuesta_id=6)
		for apuesta in apuestas:
			detalle_apuesta = DetalleApuesta.objects.filter(id_ap_id=apuesta.id,id_cab_id=instance.id_caba_id)
			for da in detalle_apuesta:
				print(da)
				apuesta.estatus='D'
				apuesta.save()
				t = Transaccion() ##Crea una transacción...
				usuario = User.objects.get(id=apuesta.usuario_id) ##Necesito el usuario que ganó, obviamente
				usuario.incrementarSaldo(apuesta.idTrans.monto, usuario.username) ##Incrementa el saldo por devolución
				t.usua = usuario ##Le asignas el usuario a la transacción
				t.fecha = datetime.now() ##La fecha del reparto
				t.monto = apuesta.idTrans.monto ##Cuánto ganó
				t.tipo = 'c' ##Crédito
				t.estado = 'c' ##Operación completada
				t.descripcion = 5 ##"Devolución de Apuesta"
				t.ref = "-" ##Referencia
				t.save() ##Guarda la transacción en la BD
		return super().form_valid(form) 

class ListaDetallesCarrJ(AuthenticatedEncarMixin, ListView):
	model = DetallesCarrera
	second_model = Carrera
	template_name = "carrera/listaDetCarr.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ListaDetallesCarrJ, self).get_context_data(**kwargs)
		context['competidores'] = DetallesCarrera.objects.filter(id_carr=pk).order_by('posicion')
		context['carrera'] = Carrera.objects.get(id=pk)
		return context

class RegistrarResultados(AuthenticatedEncarMixin, UpdateView):
	model = DetallesCarrera
	form_class = RegistrarResultadosForm
	template_name = 'carrera/registrarR.html'
	
	def get_success_url(self):
		return reverse_lazy('detalleCJ', kwargs={'pk': self.object.id_carr.id })

	def form_valid(self, form):
		instance = form.save(commit=False)
		pk = self.kwargs.get('pk')
		dt = DetallesCarrera.objects.get(id=pk).id_carr.id
		validacionpublicar = DetallesCarrera.objects.extra(select={ 
			'esperado': "count(id)",
			'guardado': "count(posicion)",
		}, where={
			"estatus = 'a'",
			"id_carr_id=%s"
		}, params={dt})
		for vp in validacionpublicar:
			if vp.esperado == vp.guardado:
				c = Carrera.objects.get(id=dt)
				c.publicable = True
				c.save()
			else:
				c = Carrera.objects.get(id=dt)
				c.publicable = False
				c.save()
		return super().form_valid(form)
	
class listadoCarreras(ListView):
	model = Carrera
	template_name = "apuesta/listadoCarreras.html"
	
	def get_context_data(self, **kwargs):
		est = self.kwargs.get('estatus')
		context = super(listadoCarreras, self).get_context_data(**kwargs)
		context["object_list"] = Carrera.objects.filter(id_jh__estatus='a')
		return context

class ConsultarC(DetailView):
	model = Carrera
	template_name = "carrera/ConsultarC.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(ConsultarC, self).get_context_data(**kwargs)
		context['object_list'] = DetallesCarrera.objects.filter(id_carr_id=pk).order_by('posicion', 'numero')
		return context

def RegistrarApuestaGanada(usuario, apuesta, mult=1, monto=0):
	t = Transaccion() ##Crea una transacción...
	if monto==0:
		usuario.incrementarSaldo(apuesta.idTrans.monto*apuesta.cuota*mult, usuario.username) ##¡Incrementa el saldo, ganó!
	else:
		usuario.incrementarSaldo(monto, usuario.username) ##¡Incrementa el saldo, ganó!
	t.usua = usuario ##Le asignas el usuario a la transacción
	t.fecha = datetime.now() ##La fecha del reparto
	if monto==0:
		t.monto = apuesta.idTrans.monto*apuesta.cuota*mult ##Cuánto ganó
	else:
		t.monto = monto
	t.tipo = 'c' ##Crédito
	t.estado = 'c' ##Operación completada
	t.descripcion = 4 ##"Apuesta ganada"
	t.ref = "-" ##Referencia
	t.save() ##Guarda la transacción en la BD
	apuesta.estatus = 'G'
	apuesta.idTransGanada = t
	apuesta.save() ##¡La apuesta ganó!

def RegistrarApuestaPerdida(apuesta):
	apuesta.estatus = 'P' 
	apuesta.save() ##La apuesta perdió :(
	
class PublicarResultados(AuthenticatedEncarMixin, UpdateView):
	model = Carrera
	form_class = FinalizarCarreraForm
	template_name = 'carrera/publicarC.html'
	def get_success_url(self):
		return reverse_lazy('listaCr')

	def form_valid(self, form): ###Una vez publicados los resultados, es hora de... ¡Escrutinios!
	###Por la forma en que lo planteo, realiza escrutinios Y reparte premios al mismo tiempo.
	###Hace un escrutinio por cada tipo de apuesta, buscando a los ganadores.
	###Comencemos
		instance = form.save(commit=False)
		id_carrera = instance.id ###¿Sobre cuál carrera trabajamos?
		caballos = DetallesCarrera.objects.filter(id_carr_id=id_carrera).exclude(posicion=500).order_by('posicion') ###¿Cuáles son los caballos en cuestión? Ordenados por llegada.
		caballo_primero = caballos[:1].get().id_caba ###El primer caballo...
		caballo_segundo = caballos[1:2].get().id_caba ###El segundo caballo...
		caballo_tercero = caballos[2:3].get().id_caba ###El tercer caballo...
		caballo_cuarto = caballos[3:4].get().id_caba ###El cuarto caballo...

		apostadores = Apuesta.objects.filter(id_carr_id=id_carrera, estatus='A') ###Vamos a buscar a todos los que apostaron en esta carrera en específico.
		
		###APUESTAS TIPO: UNICARRERA
		###Para las apuestas uni carrera.

		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 1: Ganador
		###En Ganador, se apuesta sólo a un caballo que resulte ganador de una carrera específica.

		apostadores_apGanador = apostadores.filter(tApuesta_id=1) ###...y a estos, los filtramos por los que apostaron a Ganador
		for ag in apostadores_apGanador: ###tráete el detalle de la apuesta de todos los apostadores en cuestión
			###Como es apuesta ganador, sólo se trae un objeto (get)
			detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=ag.id)
			if detalles_apuesta.id_cab == caballo_primero: ##Si el caballo del primer lugar es el mismo caballo al que apostaste, entonces...
				RegistrarApuestaGanada(User.objects.get(id=ag.usuario_id),ag)
			else:
				RegistrarApuestaPerdida(ag)
	
		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 2: Exacta
		###En el caso de exacta, se trata de de que los dos caballos elegidos terminen en 1ra y 2da posición.

		apostadores_apExacta = apostadores.filter(tApuesta_id = 2) ##Tipo de Apuesta Exacta

		for ae in apostadores_apExacta:
			detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=ae.id).order_by('posicion') ##Extraigo todos los detalle apuesta de esa apuesta. Ordeno por posicion.
			if detalles_apuesta[:1].get().id_cab == caballo_primero and detalles_apuesta[1:2].get().id_cab == caballo_segundo: ##Si pegó ambas, entonces...
				RegistrarApuestaGanada(User.objects.get(id=ae.usuario_id),ag)
			else:
				RegistrarApuestaPerdida(ae)

		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 3: Trifecta
		###Acertar el primer, segundo y tercer lugar exactos.

		apostadores_apTrifecta = apostadores.filter(tApuesta_id = 3) ##Tipo de Apuesta Trifecta

		for at in apostadores_apTrifecta:
			detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=at.id).order_by('posicion') ##Extraigo todos los detalle apuesta de esa apuesta. Ordeno por posicion.
			if detalles_apuesta[:1].get().id_cab == caballo_primero and detalles_apuesta[1:2].get().id_cab == caballo_segundo and detalles_apuesta[2:3].get().id_cab == caballo_tercero: ##Si pegó las tres, entonces...
				RegistrarApuestaGanada(User.objects.get(id=at.usuario_id),ag)
			else:
				RegistrarApuestaPerdida(at)

		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 4: Superfecta
		###Acertar los primeros 4 lugares exactos.

		apostadores_apSuperfecta = apostadores.filter(tApuesta_id = 4) ##Tipo de Apuesta Trifecta

		for aS in apostadores_apSuperfecta:
			detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=aS.id).order_by('posicion') ##Extraigo todos los detalle apuesta de esa apuesta. Ordeno por posicion.
			if detalles_apuesta[:1].get().id_cab == caballo_primero and detalles_apuesta[1:2].get().id_cab == caballo_segundo and detalles_apuesta[2:3].get().id_cab == caballo_tercero and detalles_apuesta[3:4].get().id_cab == caballo_cuarto: ##Si pegó las cuatro, entonces...
				RegistrarApuestaGanada(User.objects.get(id=aS.usuario_id),aS)
			else:
				RegistrarApuestaPerdida(aS)

		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 5: Place
		###Acertar el primer o segundo lugar

		apostadores_apPlace = apostadores.filter(tApuesta_id = 5) ##Tipo de Apuesta Place

		for al in apostadores_apPlace:
			detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=al.id)##Sólo elegí un caballo.
			if detalles_apuesta.id_cab == caballo_primero or detalles_apuesta.id_cab == caballo_segundo: ##Si pegó que llegó primero o segundo las cuatro, entonces...
				RegistrarApuestaGanada(User.objects.get(id=al.usuario_id),al)
			else:
				RegistrarApuestaPerdida(al)

		###REPARTICIÓN DE PREMIOS - TIPO DE APUESTA 6: Show
		###Acertar el primer, segundo lugar o tercer lugar

		apostadores_apShow = apostadores.filter(tApuesta_id = 6) ##Tipo de Apuesta Place

		for ah in apostadores_apShow:
			detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=ah.id)##Sólo elegí un caballo.
			if detalles_apuesta.id_cab == caballo_primero or detalles_apuesta.id_cab == caballo_segundo or detalles_apuesta.id_cab == caballo_tercero: ##Si pegó que llegó primero o segundo las cuatro, entonces...
				RegistrarApuestaGanada(User.objects.get(id=ah.usuario_id),ah)
			else:
				RegistrarApuestaPerdida(ah)

		###MULTICARRERAS
		###5y6, PollaMax. Lo primero es saber si la carrera pertenece a alguno de estos tipos de apuesta.

		jornada = JornadaH.objects.get(id=instance.id_jh_id) ##Necesito traerme la jornada hípica.
		carreras_jornada = Carrera.objects.filter(id_jh=jornada).order_by('-hora') ##Todas las carreras de la jornada, ordenadas de la última a la primera.
		carreras_5y6 = carreras_jornada[:6] ##Tengo las últimas 6 carreras de la jornada, las que aplican a 5y6 y pollamax juntas.
		carrera_polla = carreras_jornada[6:7].get() ##Tengo la 7ma última carrera de la jornada, que aplican a pollamax
		ultima_carrera = carreras_jornada[:1].get() ##Tengo la última carrera de la jornada, para repartir premios tanto de pollamax como de 5y6

		apostadores_ap5y6 = apostadores.filter(tApuesta_id=7) ##Tipo de apuesta 5y6
		apostadores_pollamax = apostadores.filter(tApuesta_id=8) ##Tipo de apuesta Polla Max

		for carrera in carreras_5y6:
			if carrera == instance: ##¿La carrera está en 5y6? Entonces reparte premios de 5y6 y pollamax.
				for a5 in apostadores_ap5y6: ##Recorro cada una de las apuestas que hay de 5y6
					detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=a5.id) ##Me traigo todos los detalle_apuesta que puede tener
					for da in detalles_apuesta: ##Recorro todos los detalle_apuesta
						if da.id_cab == caballo_primero: ##¿El caballo del detalle_apuesta es el ganador?
							da.posicion = 100 ##En efecto, el detalle_apuesta resultó ganador. Después contaré la cantidad que resultó.
							da.save()

				for am in apostadores_pollamax: ##Recorro cada una de las apuestas que hay de polla max
					detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=am.id) ##Me traigo todos los detalles
					for da in detalles_apuesta: ##Recorro todos los detalle_apuesta
						if da.id_cab == caballo_primero: ##El caballo ganó.
							da.monto = 5 ##Le asigno 5 pts
							da.save()
						elif da.id_cab == caballo_segundo: ##El segundo lugar.
							da.monto == 2 ##Le asigno 2 pts
							da.save()
						elif da.id_cab == caballo_tercero: ##El tercer lugar
							da.monto == 1 ##Le asigno 1 pt
							da.save()
						else:
							da.monto == 0 ##No tuvo puntos
							da.save()

		if instance==carrera_polla: ##Si la carrera es la 7ma última (PollaMax)
			for am in apostadores_pollamax: ##Recorro cada una de las apuestas que hay de polla max
				detalles_apuesta = DetalleApuesta.objects.get(id_ap_id=am.id) ##Me traigo todos los detalles
				for da in detalles_apuesta: ##Recorro todos los detalle_apuesta
					if da.id_cab == caballo_primero: ##El caballo ganó.
						da.monto = 5 ##Le asigno 5 pts
						da.save()
					elif da.id_cab == caballo_segundo: ##El segundo lugar.
						da.monto == 2 ##Le asigno 2 pts
						da.save()
					elif da.id_cab == caballo_tercero: ##El tercer lugar
						da.monto == 1 ##Le asigno 1 pt
						da.save()
					else:
						da.monto == 0 ##No tuvo puntos
						da.save()

		###################################################################################
		
		##Lista la repartición individual. Ahora vamos a comenzar con las reparticiones de la última carrera de la jornada
		##(de la apuesta multicarrera)
		
		if instance == ultima_carrera: ##Si estamos en la última carrera de la jornada...
			jornada.estatus = 'f' ##Registro la jornada como finalizada
			jornada.save() ##Guardo en la BD
			for ap5 in apostadores_ap5y6: ##Recorro los apostadores. (5y6)
				detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=ap5.id) ##Extraigo los detalleapuesta.
				count = 0 ##Debo contar la cantidad de veces que lo logró pegar la apuesta.
				for da in detalles_apuesta: ##Itero.
					if da.posicion == 100: ##En efecto la pegó.
						count+=1 ##Incremento el conteo
				##Ahora, verificamos si en efecto ganó.
				if count==5: ##Si logró acertar 5, ¡ganó!
					RegistrarApuestaGanada(User.objects.get(id=ap5.usuario_id),ap5,mult=0.75)
				elif count==6: ##Acertó las 6, ganó premio completo.
					RegistrarApuestaGanada(User.objects.get(id=ap5.usuario_id),ap5)
				else:
					RegistrarApuestaPerdida(ap5)
			##Para el reparto de premios de PollaMax, debemos calcular primero el pote y cuánto le corresponde a cada uno.
			pote = 0 #Inicializo
			for ap in apostadores_pollamax:
				pote += ap.monto ##Incremento en el monto

			##Ahora que está listo el pote, procedemos a contar cuántas personas ganaron. Ganan cuando la puntuación es mayor a 30.
			pote = pote * 0.75 #Este es el pote final (75% de lo ingresado)
			ganadores = 0 #Cuántas personas ganaron

			for ap in apostadores_pollamax: #Vamos a contar cuántas personas ganaron
				detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=ap.id) ##Extraigo los detalleapuesta.
				count = 0 ##Debo contar la puntuación que obtuvo
				for da in detalles_apuesta: ##Itero.
					count += da.monto
				if count > 30: #Si obtuvo más de 30 puntos, el usuario ganó
					ganadores += 1 ##Cuento
			monto = pote / ganadores ##El monto verdadero a pagarle a cada uno
			##Ahora tengo la cantidad final. Procedo a repartir (finalmente)
			for ap in apostadores_pollamax: #Vamos a ver quiénes ganaron
				detalles_apuesta = DetalleApuesta.objects.filter(id_ap_id=ap.id) ##Extraigo los detalleapuesta.
				count = 0 ##Debo contar la puntuación que obtuvo
				for da in detalles_apuesta: ##Itero.
					count += da.monto
				if count > 30: #Si obtuvo más de 30 puntos, el usuario ganó
					RegistrarApuestaGanada(User.objects.get(id=ap.usuario_id),ap,monto=monto)
				else:
					RegistrarApuestaPerdida(ap)
		##Fin del algoritmo.
		return super().form_valid(form)

