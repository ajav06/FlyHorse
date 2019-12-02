from apps.jornada.models import Carrera
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import (RegistrarForm, ActualizarNivelFrom, ActualizarFrom, GestionarTransaccionForm, 
					ConsultarTransaccionForm, SuspenderUsuarioForm)
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import User
from django.views.generic.detail import DetailView
from apps.monedavirtual.models import Transaccion, Banco
from apps.monedavirtual.forms import RegistrarBancoForm, RegistrarTransaccionForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.utils import timezone
import datetime
from django.contrib.auth.views import LogoutView, LoginView
from flyhorse.mixin import (LastAccessMixin, LoginAuthenticatedMixin, LoginRequiredMixin,
							AuthenticatedAdminMixin, AuthenticatedTransMixin, AuthenticatedUserMixin,
                            AuthorizedUserMixin, AuthorizedUser2Mixin, AuthorizedUser3Mixin)
from apps.monedavirtual.models import MonedaVirtual
# Create your views here.

"""
NOTA: Para la utilizacion de los Mixins en las vistas 
basadas en clases primero entra como parametro la Mixin 
y despues la Vista Generica
"""

"""
ADMINISTRADOR
"""

def fechaHoy(self):
	today = datetime.date.today()
	ano = str(today.year)

	if today.month < 10:
		mes = '0' + str(today.month)
	else:
		mes = str(today.month)

	if today.day < 10:
		dia = '0' + str(today.day)
	else:
		dia = str(today.day)
	
	return ano + '-' + mes + '-' + dia

def udeMes(self):
	today = datetime.date.today()
	ano = str(today.year)

	if today.month < 10:
		mes = '0' + str(today.month)
	else:
		mes = str(today.month)
	
	return ano + '-' + mes + '-01'


class ListaUsuarios(AuthenticatedAdminMixin, ListView):
	model = User
	template_name = "administrador/listaU.html"
	
	def get_context_data(self, **kwargs):
		context = super(ListaUsuarios, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context


class TransaccionesPendientes(AuthenticatedTransMixin, ListView):
	model = Transaccion
	template_name = "administrador/transPendientes.html"

	def get_context_data(self, **kwargs):
		context = super(TransaccionesPendientes, self).get_context_data(**kwargs)
		context['object_list'] = Transaccion.objects.filter(estado='e')
		context['hoy'] = fechaHoy(self)
		context['1demes'] = udeMes(self)
		return context


class TransaccionesAprobadas(AuthenticatedTransMixin, ListView):
	model = Transaccion
	template_name = "administrador/transAprobadas.html"

	def get_context_data(self, **kwargs):
		context = super(TransaccionesAprobadas, self).get_context_data(**kwargs)
		context['object_list'] = Transaccion.objects.filter(estado='a')
		context['hoy'] = fechaHoy(self)
		context['1demes'] = udeMes(self)
		return context

class TransaccionesRechazadas(AuthenticatedTransMixin, ListView):
	model = Transaccion
	template_name = "administrador/transRechazadas.html"
	
	def get_context_data(self, **kwargs):
		context = super(TransaccionesRechazadas, self).get_context_data(**kwargs)
		context['object_list'] = Transaccion.objects.filter(estado='r')
		context['hoy'] = fechaHoy(self)
		context['1demes'] = udeMes(self)
		return context

class GestionarTransaccion(AuthenticatedTransMixin, UpdateView):
	model = Transaccion
	form_class = GestionarTransaccionForm
	template_name = "administrador/gestionarT.html"
	success_url = reverse_lazy('consulta')

	def form_valid(self, form):
		instance = form.save(commit=False)
		u = User()
		if form.cleaned_data['estado'] == 'a':
			if form.cleaned_data['tipo']=='c':
				u.incrementarSaldo(form.cleaned_data['monto'], form.cleaned_data['usua']) 
			elif form.cleaned_data['tipo']=='d':
				u.disminuirSaldo(form.cleaned_data['monto'], form.cleaned_data['usua'])
		return super().form_valid(form)

class ConsultarTransaccion(AuthenticatedTransMixin, DetailView):
	model = Transaccion
	template_name = "administrador/consultarT.html"
	form_class = ConsultarTransaccionForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ConsultarTransaccionUsuario(AuthenticatedUserMixin, DetailView):
	model = Transaccion
	template_name = "consulta/consultarT.html"

"""
GLOBLAL
"""

class IniciarSesion(LoginAuthenticatedMixin, LoginView):
	template_name = 'registration/login.html'

class Inicio(LoginRequiredMixin, ListView):
	model = Carrera
	template_name = 'base/inicio.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["carreras"] = Carrera.objects.filter(estatus='p').order_by('-id_jh__fecha','-hora')[:5]
		return context


class CerrarSesion(LastAccessMixin, LogoutView):
	template_name = 'registration/logged_out.html'	

class Estadistica(AuthorizedUser3Mixin, TemplateView):
    template_name = 'inicio/estadistica.html'

class Consultar(AuthorizedUser2Mixin, TemplateView):
    template_name = 'inicio/consulta.html'

class Reglamento(AuthenticatedUserMixin, TemplateView):
    template_name = 'usuario/reglamento.html'

class Configuraciones(LoginRequiredMixin, TemplateView):
    template_name = 'configuracion/configuracion.html'

class Incluir(AuthorizedUserMixin, TemplateView):
    template_name = 'inicio/incluir.html'

class Gestionar(AuthorizedUserMixin, TemplateView):
    template_name = 'inicio/gestionar.html'

class Saldo(AuthenticatedUserMixin, TemplateView):
    template_name = 'consulta/saldo.html'

    def get_context_data(self, **kwargs):
        context = super(Saldo, self).get_context_data(**kwargs)
        context['moneda_v'] = MonedaVirtual.objects.all().order_by('-fecha')[0]
        return context

def signInDone(request):
	return render(request, 'registration/signIn_done.html', {})

class Transacciones(AuthenticatedUserMixin, ListView):
	model = Transaccion
	template_name = "consulta/transaccion.html"
       
	def get_context_data(self, **kwargs):
		context = super(Transacciones, self).get_context_data(**kwargs)
		context['object_list'] = Transaccion.objects.filter(usua_id=self.request.user.id).order_by('-fecha','ref')
		context['hoy'] = fechaHoy(self)
		context['1demes'] = udeMes(self)
		return context

class RegistrarTransC(AuthenticatedUserMixin, CreateView):
	model = Transaccion
	form_class = RegistrarTransaccionForm
	template_name = "consulta/retirar.html"
	def get_success_url(self):
		return reverse_lazy('trans', kwargs={'modal': 'show'})

	def get_context_data(self, **kwargs):
		context = super(RegistrarTransC, self).get_context_data(**kwargs)
		context['bancos'] = Banco.objects.filter(usua_id=self.request.user.id)
		context['moneda_v'] = MonedaVirtual.objects.all().order_by('-fecha')[0]
		return context

class RegistrarTransD(AuthenticatedUserMixin, CreateView):
	model = Transaccion
	form_class = RegistrarTransaccionForm
	template_name = "consulta/recargar.html"
	
	def get_context_data(self, **kwargs):
		context = super(RegistrarTransD, self).get_context_data(**kwargs)
		context['moneda_v'] = MonedaVirtual.objects.all().order_by('-fecha')[0]
		return context

	def get_success_url(self):
		return reverse_lazy('trans', kwargs={'modal': 'show'})


class ModificarUser(AuthenticatedAdminMixin, UpdateView):
	model = User
	form_class = ActualizarNivelFrom
	template_name = "administrador/actualizarNU.html"
	
	def get_success_url(self):
		return reverse_lazy('listaU', kwargs={'modal': 'show'})

class SuspenderUsuario(AuthenticatedAdminMixin, UpdateView):
	model = User
	form_class = SuspenderUsuarioForm
	template_name = "administrador/suspenderU.html"
	
	def get_success_url(self):
		return reverse_lazy('listaU', kwargs={'modal': 'show'})

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.is_active = False
		return super().form_valid(form)

class RegistrarUsuario(CreateView):
	model = User
	form_class = RegistrarForm
	template_name = "usuario/signIn.html"
	success_url = reverse_lazy('signIn_done')

class ActualizarUser(LoginRequiredMixin, UpdateView):
	model = User
	form_class = ActualizarFrom
	template_name = "configuracion/actualizarDatos.html"
	success_url = reverse_lazy('configuraciones')

class RegistrarBanco(AuthenticatedUserMixin, CreateView):
	model = Banco
	form_class = RegistrarBancoForm
	template_name = "consulta/banco.html"

	def get_success_url(self):
          return reverse_lazy('retir')

class ModificarBanco(AuthenticatedUserMixin, UpdateView):
	model = Banco
	form_class = RegistrarBancoForm
	template_name = "consulta/modBanco.html"

	def get_success_url(self):
          pk=self.kwargs['pk']
          return reverse_lazy('modiB', kwargs={'pk': pk})

class ListaBanco(AuthenticatedUserMixin, ListView):
	model = Banco
	template_name = "consulta/listaB.html"

	def get_context_data(self, **kwargs):
		context = super(ListaBanco, self).get_context_data(**kwargs)
		context['object_list'] = Banco.objects.filter(usua_id=self.request.user.id)
		return context

class EstadisticasRS(AuthenticatedAdminMixin, ListView):
	model = User
	template_name = "administrador/estadR.html"

	def get_context_data(self, **kwargs):
		context = super(EstadisticasRS, self).get_context_data(**kwargs)
		ingresos_brutos = Transaccion.objects.extra(select={
			'sum':"sum(monto)"
		}, where={
			'descripcion=1',
			'estado=\'a\''
		}
		)[0].sum

		pagos_totales = Transaccion.objects.extra(select={
			'sum':"sum(monto)"
		}, where={
			'descripcion=2',
			'estado=\'a\''
		}
		)[0].sum

		cant_token = User.objects.extra(select={
			'sum':"sum(balance)"
		}, where={
			'is_active=1'
		})[0].sum

		pagos_totales_recibidos = Transaccion.objects.filter(descripcion=1,estado='a').count() 

		pagos_divisas = Transaccion.objects.filter(descripcion=1,bco='BOFA',estado='a') | Transaccion.objects.filter(descripcion=1,bco='WF',estado='a') | Transaccion.objects.filter(descripcion=1,bco='ZL',estado='a')
		pagos_divisas_recibidos = pagos_divisas.count()

		pagos_totales_emitidos = Transaccion.objects.filter(descripcion=2,estado='a').count() 

		pagos_divisas = Transaccion.objects.filter(descripcion=2,bco_retiro__bco='BOFA',estado='a') | Transaccion.objects.filter(descripcion=2,bco_retiro__bco='WF',estado='a') | Transaccion.objects.filter(descripcion=2,bco_retiro__bco='ZL',estado='a')
		pagos_divisas_emitidos = pagos_divisas.count()

		if pagos_totales!=None:
			context['pagos_totales'] = pagos_totales_emitidos
		else:
			context['pagos_totales'] = 0

		if ingresos_brutos!=None:
			context['ingresos_brutos'] = ingresos_brutos
		else:
			context['ingresos_brutos'] = 0
		
		if ingresos_brutos!=None and pagos_totales!=None:
			context['ganancia_neta'] = ingresos_brutos-pagos_totales
		elif ingresos_brutos==None and pagos_totales!=None:
			context['ganancia_neta'] = -pagos_totales
		elif pagos_totales==None and ingresos_brutos!=None:
			context['ganancia_neta'] = ingresos_brutos
		else:
			context['ganancia_neta'] = ingresos_brutos-pagos_totales

		context['cant_token'] = cant_token
		if pagos_divisas_recibidos!=None and pagos_totales_recibidos!=None and pagos_totales_recibidos!=0:
			context['porc_pagos_recibidos_divisas'] = pagos_divisas_recibidos / pagos_totales_recibidos * 100
		else:
			context['porc_pagos_recibidos_divisas'] = 0

		if pagos_divisas_emitidos!=None and pagos_totales_emitidos!=None and pagos_totales_emitidos!=0:
			context['porc_pagos_emitidos_divisas'] = pagos_divisas_emitidos / pagos_totales_emitidos * 100
		else:
			context['porc_pagos_emitidos_divisas'] = 0
		return context
