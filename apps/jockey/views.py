from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import IncluirJockeyForm, ModificarJockeyForm
from .models import Jockey
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.jornada.models import *
from flyhorse.mixin import AuthenticatedAdminMixin
import math
# Create your views here.

class IncluirJockey(AuthenticatedAdminMixin, CreateView):
	model = Jockey
	form_class = IncluirJockeyForm
	template_name = "jockey/incluirJ.html"
	
	def get_success_url(self):
		return reverse_lazy('incluirJk', kwargs={'modal': 'show'})

	def get_context_data(self, **kwargs):
		context = super(IncluirJockey, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context


class ListaJockeys(AuthenticatedAdminMixin, ListView):
	model = Jockey
	template_name = "jockey/listaJ.html"

	def get_context_data(self, **kwargs):
		context = super(ListaJockeys, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context

class ActualizarJockey(AuthenticatedAdminMixin, UpdateView):
	model = Jockey
	form_class = ModificarJockeyForm
	template_name = "jockey/actualizarJ.html"

	def get_success_url(self):
		return reverse_lazy('listaJk', kwargs={'modal': 'show'})

class EliminarJockey(AuthenticatedAdminMixin, DeleteView):
	model = Jockey
	template_name = "jockey/eliminarJ.html"

	def get_success_url(self):
		return reverse_lazy('listaJk', kwargs={'modal': 'show'})

class EstadisticasJockey(DetailView):
	model = Jockey
	template_name = "jockey/estadJ.html"

	def get_context_data(self, **kwargs):
		context = super(EstadisticasJockey, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk') ###Clave del Jockey

		pm = '%.3f'%DetallesCarrera.objects.extra(select={ ###Promedio de posición del jockey
				'promedio': "AVG(posicion)"
			}, where={
				"id_jock_id = %s",
				"estatus='a'",
				"posicion != 500"
			}, params={pk})[0].promedio

		###VARIACION DE POSICION
		###Probablemente el método más complicado de las estadísticas del caballo.
		###Realiza cálculos en las siguientes etapas:
		###(1) Media (ya calculada como pm)
		###(2) Buscar todas las posiciones del caballo en cuestión
		###(3) Contar la cantidad de carreras que ha corrido el caballo = N
		###(4) Calcular sum = Σ|x-x¯|^2
		###(5) Calcular desviacion = √(sum/N)
		###NOTA: '%.3f'% trunca a 3 decimales los valores.
		pos = DetallesCarrera.objects.extra(select={ ### (2) posiciones del caballo
				'posicion': "posicion"
			}, where={
				"estatus = 'a'",
				"id_jock_id = %s",
				"posicion != 500"
			}, params={pk})

		N = DetallesCarrera.objects.extra(select={ ### (3) cantidad de carreras
				'cant': "COUNT(posicion)"
			}, where={
				"estatus = 'a'",
				"id_jock_id = %s",
				"posicion != 500"
			}, params={pk})
		for n in N:
			Nn = int(n.cant)

		sum = 0
		for p in pos:
			if (str(p.posicion!='') or p.posicion!=None or p.posicion!=500):
				sum = sum + math.pow((int(p.posicion) - float(pm)),2) ###sumatoria
			
		if Nn != 0: ### valido para no dividir entre 0
			desv = math.sqrt(sum / Nn)
		else:
			desv = 0

		desv = '%.3f'%desv

		###Caballo más ganador

		###Primero definimos con cuáles caballos ha corrido el jockey

		caballos_jockey = DetallesCarrera.objects.filter(id_jock_id=pk, id_caba__estatus='a').values_list('id_caba_id', flat=True).distinct()

		mayor=0
		id_mayor=0
		for cj in caballos_jockey: ###Itero sobre todos los caballos, buscando cuántas carreras ha ganado con este caballo y comparando con un mayor
			cant_carr = DetallesCarrera.objects.filter(id_jock_id=pk,id_caba_id=cj,posicion=1).count()
			if cant_carr>mayor:
				mayor=cant_carr
				id_mayor=cj

		context['caballo_mayor'] = Caballo.objects.get(id=id_mayor)
		context['promedio'] = pm
		context['desviacion'] = desv
		return context
