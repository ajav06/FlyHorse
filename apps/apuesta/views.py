from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import TipoApuesta
from apps.hipodromo.models import Hipodromo
from apps.caballo.models import Caballo 
from apps.apuesta.models import Apuesta, DetalleApuesta
from apps.jornada.models import Carrera, JornadaH, DetallesCarrera
from apps.usuario.models import User
from django.shortcuts import get_object_or_404
from flyhorse.mixin import AuthenticatedUserMixin
from django.views.generic.base import View, TemplateView
from django.shortcuts import render, redirect
from .forms import MultiplesForm, RegistrarApuFrom, RegistrarTransApuForm, RegistrarDetaApuFrom, MultiplesForm5y6
from django.urls import reverse_lazy
from apps.monedavirtual.models import Transaccion
from django.views.generic.edit import FormView
from django.db.models import Sum

class ConsultarAp(AuthenticatedUserMixin, ListView):
     model = Apuesta
     template_name = "apuesta/listadoApuestas.html"

class Apostar(AuthenticatedUserMixin, ListView):
    model = Hipodromo
    template_name = "apuesta/Apostar_base.html"

    def get_context_data(self, **kwargs):
        context = super(Apostar, self).get_context_data(**kwargs)
        context['show'] = self.kwargs.get('modal')
        return context

class SelecTipoApuesta(AuthenticatedUserMixin, ListView):
    model = Carrera
    second_model = Hipodromo
    third_model = JornadaH
    template_name = "apuesta/selecTipoApuesta.html"

    def get_queryset(self):
        return Hipodromo.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(SelecTipoApuesta, self).get_context_data(**kwargs)
        context['jornada'] = JornadaH.objects.all().order_by('-fecha')[0]
        context['carreras'] = Carrera.objects.filter(id_jh__id_hip=pk, id_jh__estatus='a',id_jh=context['jornada'].id).order_by('hora')
        context['hip'] = Hipodromo.objects.get(id=pk)
        return context

class Apuesta_Unicarrera(AuthenticatedUserMixin, ListView):
    model = Carrera
    second_model = Hipodromo
    third_model = TipoApuesta
    template_name = "apuesta/Ap_Unicarrera.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        context = super(Apuesta_Unicarrera, self).get_context_data(**kwargs)
        context['jornada'] = JornadaH.objects.all().order_by('-fecha')[0]
        context['carreras'] = Carrera.objects.filter(id_jh__id_hip=pk,id_jh__estatus='a',id_jh=context['jornada'].id)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)
        return context

class Apuesta_Unicarrera_selec(AuthenticatedUserMixin, ListView):
    model = DetallesCarrera
    second_model = Hipodromo
    third_model = TipoApuesta
    template_name = "apuesta/Ap_Unicarrera.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        context = super(Apuesta_Unicarrera_selec, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.filter(id_jh__id_hip=pk,id_jh__estatus='a').order_by('hora')
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)
        return context

class Apuesta_Ganador(AuthenticatedUserMixin, CreateView):
    model = DetallesCarrera
    second_model = Hipodromo
    third_model = JornadaH
    template_name = "apuesta/Ap_Ganador.html"
    form_class = MultiplesForm
    success_url = reverse_lazy('apostar')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Ganador, self).get_context_data(**kwargs)
        context['jornada'] = JornadaH.objects.all().order_by('-fecha')[0]
        context['carreras'] = Carrera.objects.filter(id=carr,id_jh__estatus='a')[0]
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)
        return context

class Apuesta_Exacta(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Exacta.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        des2 = form['detaAp2'].save(commit=False)
        des2.montoD = trans.monto
        des2.id_ap = apuesta
        des2.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Exacta, self).get_context_data(**kwargs)
        multiplicadores_id = []
        context['carreras'] = Carrera.objects.get(id=carr)
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)
        
        multiplicadores_id = []
        multiplicadores_primero = []
        multiplicadores_segundo = []

        caballos_multiplicadores = context['detalle'].filter(estatus='a').order_by('numero')

        for caballo in caballos_multiplicadores:
            multiplicadores_id.append(caballo.id_caba_id)
            mult1 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count()
                mult1 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_primero.append(str('%.3f'%mult1).replace(',', '.'))

            mult2 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count()
                mult2 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_segundo.append(str('%.3f'%mult2).replace(',', '.'))


        context['multiplicadores_id'] = multiplicadores_id
        context['multiplicadores_primero'] = multiplicadores_primero
        context['multiplicadores_segundo'] = multiplicadores_segundo
        return context

    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_Trifecta(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Trifecta.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        des2 = form['detaAp2'].save(commit=False)
        des2.montoD = trans.monto
        des2.id_ap = apuesta
        des2.save()
        des3 = form['detaAp3'].save(commit=False)
        des3.montoD = trans.monto
        des3.id_ap = apuesta
        des3.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Trifecta, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.get(id=carr)
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        multiplicadores_id = []
        multiplicadores_primero = []
        multiplicadores_segundo = []
        multiplicadores_tercero = []

        caballos_multiplicadores = context['detalle'].filter(estatus='a').order_by('numero')

        for caballo in caballos_multiplicadores:
            multiplicadores_id.append(caballo.id_caba_id)
            mult1 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count()
                mult1 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_primero.append(str('%.3f'%mult1).replace(',', '.'))

            mult2 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count()
                mult2 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_segundo.append(str('%.3f'%mult2).replace(',', '.'))

            mult3 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=3,estatus='a',id_carr__estatus='p').count()
                mult3 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_tercero.append(str('%.3f'%mult3).replace(',', '.'))


        context['multiplicadores_id'] = multiplicadores_id
        context['multiplicadores_primero'] = multiplicadores_primero
        context['multiplicadores_segundo'] = multiplicadores_segundo
        context['multiplicadores_tercero'] = multiplicadores_tercero

        return context
    
    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_Superfecta(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Superfecta.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        des2 = form['detaAp2'].save(commit=False)
        des2.montoD = trans.monto
        des2.id_ap = apuesta
        des2.save()
        des3 = form['detaAp3'].save(commit=False)
        des3.montoD = trans.monto
        des3.id_ap = apuesta
        des3.save()
        des4 = form['detaAp4'].save(commit=False)
        des4.montoD = trans.monto
        des4.id_ap = apuesta
        des4.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Superfecta, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.get(id=carr)
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['caballos_corriendo'] = DetallesCarrera.objects.filter(id_carr=carr, estatus='a')
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        multiplicadores_id = []
        multiplicadores_primero = []
        multiplicadores_segundo = []
        multiplicadores_tercero = []
        multiplicadores_cuarto = []

        caballos_multiplicadores = context['detalle'].filter(estatus='a').order_by('numero')

        for caballo in caballos_multiplicadores:
            multiplicadores_id.append(caballo.id_caba_id)
            mult1 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count()
                mult1 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_primero.append(str('%.3f'%mult1).replace(',', '.'))

            mult2 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count()
                mult2 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_segundo.append(str('%.3f'%mult2).replace(',', '.'))

            mult3 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=3,estatus='a',id_carr__estatus='p').count()
                mult3 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_tercero.append(str('%.3f'%mult3).replace(',', '.'))

            mult4 = 1.5
            cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total_carreras_corridas > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=4,estatus='a',id_carr__estatus='p').count()
                print(cant_total_carreras_ganadas)
                mult4 = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas
            multiplicadores_cuarto.append(str('%.3f'%mult4).replace(',', '.'))

        context['multiplicadores_id'] = multiplicadores_id
        context['multiplicadores_primero'] = multiplicadores_primero
        context['multiplicadores_segundo'] = multiplicadores_segundo
        context['multiplicadores_tercero'] = multiplicadores_tercero
        context['multiplicadores_cuarto'] = multiplicadores_cuarto

        return context
    
    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_Place(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Place.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Place, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.get(id=carr)
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        multiplicadores_id = []
        multiplicadores = []

        for caballo in context['detalle']:
            multiplicadores_id.append(caballo.id)
            cant_total = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count()
                mult1 = cant_total_carreras_ganadas/cant_total
                cant_total_carreras_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count()
                mult2 = cant_total_carreras_segundo/cant_total
                multiplicadores.append(str('%.3f'%(1.5-(mult1*mult2))).replace(',', '.'))
            else:
                multiplicadores.append(str(1.3).replace(',','.'))

        context['multiplicadores_id'] = multiplicadores_id
        context['multiplicadores'] = multiplicadores
        return context
    
    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_Show(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Show.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        carr = self.kwargs.get('carr')
        context = super(Apuesta_Show, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.get(id=carr)
        context['detalle'] = DetallesCarrera.objects.filter(id_carr=carr)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre=ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        multiplicadores_id = []
        multiplicadores = []

        for caballo in context['detalle']:
            multiplicadores_id.append(caballo.id)
            cant_total = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
            if cant_total > 5:
                cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count()
                mult1 = cant_total_carreras_ganadas/cant_total
                cant_total_carreras_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count()
                mult2 = cant_total_carreras_segundo/cant_total
                cant_total_carreras_tercero = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=3,estatus='a',id_carr__estatus='p').count()
                multiplicadores.append(str('%.3f'%(1.5-(mult1*mult2))).replace(',', '.'))
            else:
                multiplicadores.append(str(1.15).replace(',','.'))

        context['multiplicadores_id'] = multiplicadores_id
        context['multiplicadores'] = multiplicadores

        return context

    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_5y6(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm5y6
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_5y6.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des1 = form['detaAp1'].save(commit=False)
        des1.montoD = trans.monto
        des1.id_ap = apuesta
        des1.save()
        des2 = form['detaAp2'].save(commit=False)
        des2.montoD = trans.monto
        des2.id_ap = apuesta
        des2.save()
        des3 = form['detaAp3'].save(commit=False)
        des3.montoD = trans.monto
        des3.id_ap = apuesta
        des3.save()
        des4 = form['detaAp4'].save(commit=False)
        des4.montoD = trans.monto
        des4.id_ap = apuesta
        des4.save()
        des5 = form['detaAp5'].save(commit=False)
        des5.montoD = trans.monto
        des5.id_ap = apuesta
        des5.save()
        des6 = form['detaAp6'].save(commit=False)
        des6.montoD = trans.monto
        des6.id_ap = apuesta
        des6.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        context = super(Apuesta_5y6, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.filter(id_jh__id_hip=pk).filter(id_jh__estatus='a').order_by('-hora')[:6]
        context['detalle'] = DetallesCarrera.objects.filter(id_carr__id_jh__id_hip=pk)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre = ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        ##MULTIPLICADORES PARA 5y6
        ##La idea es que cada caballo tenga su cuota propia, multiplicarlas entre sí (y por 8) y así obtener la cuota de la apuesta
        ##Para ello, debemos pasar por contexto los multiplicadores de cada caballo de cada carrera.
        ##Comencemos con la carrera 1.

        carrera_1 = context['carreras'][0] #Primera carrera
        multi_carrera1 = [] #Arreglo con los multiplicadores
        detalles_c1 = context['detalle'].filter(id_carr_id=carrera_1.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c1: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera1.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        carrera_2 = context['carreras'][1] #Segunda carrera
        multi_carrera2 = [] #Arreglo con los multiplicadores
        detalles_c2 = context['detalle'].filter(id_carr_id=carrera_2.id) #Me traigo los detalles de la carrera
        for caballo in detalles_c2: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera2.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        carrera_3 = context['carreras'][2] #Tercera carrera
        multi_carrera3 = [] #Arreglo con los multiplicadores
        detalles_c3 = context['detalle'].filter(id_carr_id=carrera_3.id) #Me traigo los detalles de la carrera
        for caballo in detalles_c3: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera3.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        carrera_4 = context['carreras'][3] #Cuarta carrera
        multi_carrera4 = [] #Arreglo con los multiplicadores
        detalles_c4 = context['detalle'].filter(id_carr_id=carrera_4.id) #Me traigo los detalles de la carrera
        for caballo in detalles_c4: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera4.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        carrera_5 = context['carreras'][4] #Quinta carrera
        multi_carrera5 = [] #Arreglo con los multiplicadores
        detalles_c5 = context['detalle'].filter(id_carr_id=carrera_5.id) #Me traigo los detalles de la carrera
        for caballo in detalles_c5: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera5.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        carrera_6 = context['carreras'][5] #Sexta carrera
        multi_carrera6 = [] #Arreglo con los multiplicadores
        detalles_c6 = context['detalle'].filter(id_carr_id=carrera_6.id) #Me traigo los detalles de la carrera
        for caballo in detalles_c6: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 5: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                mult = 2 - total_ganadas/total_carreras #Fórmula de proporción para la cuota
            else:
                mult = 1.5 #1,5 si no ha participado en más de 5 carreras.
            multi_carrera6.append(str('%.3f'%mult).replace(',', '.')) #Añado a los multiplicadores de la carrera 1

        #Ahora, pasar los arreglos por contexto
        context['m1'] = multi_carrera1
        context['m2'] = multi_carrera2
        context['m3'] = multi_carrera3
        context['m4'] = multi_carrera4
        context['m5'] = multi_carrera5
        context['m6'] = multi_carrera6
        return context
   
    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class Apuesta_Loto(AuthenticatedUserMixin, ListView):
    model = TipoApuesta
    template_name =  "apuesta/Ap_5y6.html"

class Apuesta_Polla(AuthenticatedUserMixin, CreateView):
    form_class = MultiplesForm5y6
    success_url = reverse_lazy('inicio')
    template_name = "apuesta/Ap_Polla.html"

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des1 = form['detaAp1'].save(commit=False)
        des1.montoD = trans.monto
        des1.id_ap = apuesta
        des1.save()
        des2 = form['detaAp2'].save(commit=False)
        des2.montoD = trans.monto
        des2.id_ap = apuesta
        des2.save()
        des3 = form['detaAp3'].save(commit=False)
        des3.montoD = trans.monto
        des3.id_ap = apuesta
        des3.save()
        des4 = form['detaAp4'].save(commit=False)
        des4.montoD = trans.monto
        des4.id_ap = apuesta
        des4.save()
        des5 = form['detaAp5'].save(commit=False)
        des5.montoD = trans.monto
        des5.id_ap = apuesta
        des5.save()
        des6 = form['detaAp6'].save(commit=False)
        des6.montoD = trans.monto
        des6.id_ap = apuesta
        des6.save()
        des7 = form['detaAp7'].save(commit=False)
        des7.montoD = trans.monto
        des7.id_ap = apuesta
        des7.save()
        des21 = form['detaAp21'].save(commit=False)
        des21.montoD = trans.monto
        des21.id_ap = apuesta
        des21.save()
        des22 = form['detaAp22'].save(commit=False)
        des22.montoD = trans.monto
        des22.id_ap = apuesta
        des22.save()
        des23 = form['detaAp23'].save(commit=False)
        des23.montoD = trans.monto
        des23.id_ap = apuesta
        des23.save()
        des24 = form['detaAp24'].save(commit=False)
        des24.montoD = trans.monto
        des24.id_ap = apuesta
        des24.save()
        des25 = form['detaAp25'].save(commit=False)
        des25.montoD = trans.monto
        des25.id_ap = apuesta
        des25.save()
        des26 = form['detaAp26'].save(commit=False)
        des26.montoD = trans.monto
        des26.id_ap = apuesta
        des26.save()
        des27 = form['detaAp27'].save(commit=False)
        des27.montoD = trans.monto
        des27.id_ap = apuesta
        des27.save()
        u = User()
        u.disminuirSaldo(trans.monto, trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        ap = self.kwargs.get('ap')
        context = super(Apuesta_Polla, self).get_context_data(**kwargs)
        ult_jornada = JornadaH.objects.all().order_by('-fecha')[0].id
        context['carreras'] = Carrera.objects.filter(id_jh__id_hip=pk, id_jh__estatus='a',id_jh_id=ult_jornada).order_by('-hora')[:7]
        context['detalle'] = DetallesCarrera.objects.filter(id_carr__id_jh__id_hip=pk)
        context['object_list'] = Hipodromo.objects.all()
        context['tipoap'] = TipoApuesta.objects.get(nombre=ap)
        context['hip'] = Hipodromo.objects.get(id=pk)

        ###CUOTAS
        ###Evidentemente, por la forma en que las apuestas de PollaMax trabajan, no se trabaja directamente con cuotas, sino con un pote.
        ###Este pote es del 75% del monto total de las apuestas realizadas de PollaMax en la jornada.

        apuestas = Apuesta.objects.filter(tApuesta_id=8,id_jorh_id=ult_jornada) ##Todas las apuestas PollaMax presentes en la jornada actual
        suma = 0 #Sumatoria

        for apuesta in apuestas: #Necesito extraer el monto.
            suma += apuesta.idTrans.monto #Sumo todos los montos

        context['cuota'] = suma

        ###MONTO
        ###Ahora, bien, PollaMax trabaja con un monto "predefinido" en el cual un caballo tiene un cierto precio.
        ###En FlyHorse: precio = 10 + 10 * # Carreras Ganadas + 5 * # Carreras en Segundo Lugar

        carrera_1 = context['carreras'][0] #Primera carrera
        montos_carrera1 = [] #Arreglo con los montos de cada caballo
        detalles_c1 = context['detalle'].filter(id_carr_id=carrera_1.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c1: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera1.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera1.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera1.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera1.append(str('%.3f'%0))

        carrera_2 = context['carreras'][1] #Segunda carrera
        montos_carrera2 = [] #Arreglo con los montos de cada caballo
        detalles_c2 = context['detalle'].filter(id_carr_id=carrera_2.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c2: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera2.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera2.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera2.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera2.append(str('%.3f'%0))

        carrera_3 = context['carreras'][2] #Tercera carrera
        montos_carrera3 = [] #Arreglo con los montos de cada caballo
        detalles_c3 = context['detalle'].filter(id_carr_id=carrera_3.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c3: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera3.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera3.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera3.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera3.append(str('%.3f'%0))

        carrera_4 = context['carreras'][3] #Cuarta carrera
        montos_carrera4 = [] #Arreglo con los montos de cada caballo
        detalles_c4 = context['detalle'].filter(id_carr_id=carrera_4.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c4: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera4.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera4.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera4.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera4.append(str('%.3f'%0))

        carrera_5 = context['carreras'][4] #Quinta carrera
        montos_carrera5 = [] #Arreglo con los montos de cada caballo
        detalles_c5 = context['detalle'].filter(id_carr_id=carrera_5.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c5: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera5.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera5.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera5.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera5.append(str('%.3f'%0))

        carrera_6 = context['carreras'][5] #Sexta carrera
        montos_carrera6 = [] #Arreglo con los montos de cada caballo
        detalles_c6 = context['detalle'].filter(id_carr_id=carrera_6.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c6: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera6.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera6.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera6.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera6.append(str('%.3f'%0))

        carrera_7 = context['carreras'][6] #Septima carrera
        montos_carrera7 = [] #Arreglo con los montos de cada caballo
        detalles_c7 = context['detalle'].filter(id_carr_id=carrera_7.id) #Me traigo los detalles de la primera carrera
        for caballo in detalles_c7: #Recorro todos los detalles (caballos)
            total_carreras = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion__lt=500,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras del caballo
            if total_carreras > 0: #Si ha corrido más de 5 carreras...
                total_ganadas = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=1,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras ganadas
                total_segundo = DetallesCarrera.objects.filter(id_caba_id=caballo.id_caba_id,posicion=2,estatus='a',id_carr__estatus='p').count() #Cuento total de carreras en segundo lugar
            if total_ganadas != None and total_segundo != None:
                montos_carrera7.append(str('%.3f'%(10 + 10*total_ganadas + 5*total_segundo)))
            elif total_ganadas == None:
                montos_carrera7.append(str('%.3f'%(10 + 5*total_segundo)))
            elif total_segundos == None:
                montos_carrera7.append(str('%.3f'%(10 + 10*total_ganadas)))
            else:
                montos_carrera7.append(str('%.3f'%0))

        #Ahora, pasar los arreglos por contexto
        context['m1'] = montos_carrera1
        context['m2'] = montos_carrera2
        context['m3'] = montos_carrera3
        context['m4'] = montos_carrera4
        context['m5'] = montos_carrera5
        context['m6'] = montos_carrera6        
        context['m7'] = montos_carrera7
        return context

    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})

class ConsultarAp(AuthenticatedUserMixin, DetailView):
    model = Apuesta
    template_name = "apuesta/ConsultarAp.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ConsultarAp, self).get_context_data(**kwargs)
        apue = Apuesta.objects.get(id=pk)
        context['Apuesta'] = apue
        context['detalles'] = DetalleApuesta.objects.filter(id_ap=apue)
        if apue.id_carr == None:
            context['carreras'] = Carrera.objects.filter(id_jh=apue.id_jorh).filter(id_jh__estatus='a').order_by('-hora')[:7]
        return context

class listadoApuestas(AuthenticatedUserMixin, ListView):
    model = Apuesta
    template_name = "apuesta/listadoApuestas.html"

    def get_context_data(self, **kwargs):
	    context = super(listadoApuestas, self).get_context_data(**kwargs)
	    context['objects_list'] = Apuesta.objects.filter(usuario_id=self.request.user.id)
	    return context

class EstadisticasApuesta(AuthenticatedUserMixin, ListView):
    model = User
    template_name='apuesta/estadA.html'

    def get_context_data(self, **kwargs):
        context = super(EstadisticasApuesta,self).get_context_data(**kwargs)
        pk = self.request.user.id
        ganadas = Apuesta.objects.filter(estatus='G',usuario_id=pk).count()
        perdidas = Apuesta.objects.filter(estatus='P',usuario_id=pk).count()
        total = ganadas + perdidas
        if total!=0:
            porcentaje = ganadas/total*100
        else:
            porcentaje = 0

        gastado = Transaccion.objects.extra(select={
            'sum':"sum(monto)"
        }, where={
            'descripcion=3',
            'usua_id=%s',
            'estado=\'c\''
        }, params={pk})[0].sum

        ganado = Transaccion.objects.extra(select={
            'sum':"sum(monto)"
        }, where={
            'descripcion=4',
            'usua_id=%s',
            'estado=\'c\''
        }, params={pk})[0].sum

        context['porcentaje'] = porcentaje
        context['ganado'] = ganado
        
        if ganado==None:
            context['g_netas'] = -gastado
        elif gastado==None:
            context['g_netas'] = ganado
        elif ganado==None and gastado==None:
            context['g_netas'] = 0
        else:
            context['g_netas'] = ganado-gastado

        if gastado!=None:
            context['gastado'] = gastado
        else:
            context['gastado'] = 0
        return context

class ListaDetCarr(AuthenticatedUserMixin, ListView):
    model = DetallesCarrera
    second_model = Carrera
    template_name = 'apuesta/listD.html'
    def get_queryset(self):
        return Hipodromo.objects.all()
    def get_context_data(self, **kwargs):
            pk = self.kwargs.get('pk')
            context = super(ListaDetCarr, self).get_context_data(**kwargs)
            context['competidores'] = DetallesCarrera.objects.filter(id_carr=pk).order_by('posicion')
            context['carrera'] = Carrera.objects.get(id=pk)
            return context

class RegistrarApuestaGana(AuthenticatedUserMixin, View):
    template_name = 'apuesta/Ap_Ganador.html'
    def index(self,request):
        if request.method == 'POST':
            form1 = RegistrarTransApuForm(request.POST)
            form2 = RegistrarApuFrom(request.POST)
            form3 = RegistrarDetaApuFrom(request.POST)
            if form1.is_valid() and form2.is_valid() and form3.is_valid():
                form1.save()
                form2.save()
                form3.save()
            return redirect('apostar')
        else:
            form3 = RegistrarDetaApuFrom()
        return render(request, 'tick/Registro_Cliente.html', {'form': form3})

class Apuesta_Ganador_Confirmar(AuthenticatedUserMixin, CreateView):
    template_name = 'apuesta/Ap_Ganador_Confirmar.html'
    form_class = MultiplesForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        trans = form['trans'].save()
        apuesta = form['apue'].save(commit=False)
        apuesta.idTrans = trans
        apuesta.usuario = trans.usua
        apuesta.save()
        des = form['detaAp'].save(commit=False)
        des.montoD = trans.monto
        des.id_ap = apuesta
        des.save()
        u = User()
        u.disminuirSaldo(trans.monto,trans.usua.username)
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Apuesta_Ganador_Confirmar,self).get_context_data(**kwargs)
        pk = self.kwargs.get('carr')
        pk2 = self.kwargs.get('cab')

        ##CUOTA

        mult = 1.5
        cant_total_carreras_corridas = DetallesCarrera.objects.filter(id_caba_id=pk2,posicion__lt=500,estatus='a',id_carr__estatus='p').count()
        if cant_total_carreras_corridas > 5:
            cant_total_carreras_ganadas = DetallesCarrera.objects.filter(id_caba_id=pk2,posicion=1,estatus='a',id_carr__estatus='p').count()
            mult = 2 - cant_total_carreras_ganadas/cant_total_carreras_corridas

        mult = mult

        context['carr'] = Carrera.objects.get(id=pk)
        context['tp'] = self.kwargs.get('tp')
        context['caballo'] = Caballo.objects.get(id=pk2)
        context['cuota'] = str('%.3f'%mult).replace(',', '.')
        context['ge'] = mult * 100
        return context
    
    def get_success_url(self):
        return reverse_lazy('apostar', kwargs={'modal': 'show'})
