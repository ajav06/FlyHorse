from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import IncluirEntrenadorForm, ModicarEntrenadorForm
from .models import Entrenador
from apps.caballo.models import *
from apps.jornada.models import *
from django.views.generic.list import ListView
from flyhorse.mixin import AuthenticatedAdminMixin
# Create your views here.


class IncluirEntrenador(AuthenticatedAdminMixin, CreateView):
	model = Entrenador
	form_class = IncluirEntrenadorForm
	template_name = "entrenador/incluirE.html"
	
	def get_success_url(self):
		return reverse_lazy('incluirE', kwargs={'modal': 'show'})

	def get_context_data(self, **kwargs):
		context = super(IncluirEntrenador, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context

class ListaEntrenadores(AuthenticatedAdminMixin, ListView):
	model = Entrenador
	template_name ="entrenador/listaE.html"

	def get_context_data(self, **kwargs):
		context = super(ListaEntrenadores, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context

class ActualizarEntrenador(AuthenticatedAdminMixin, UpdateView):
	model = Entrenador
	form_class = ModicarEntrenadorForm
	template_name = "entrenador/actualizarE.html"
	
	def get_success_url(self):
		return reverse_lazy('listaE', kwargs={'modal': 'show'})

class EliminarEntrenador(AuthenticatedAdminMixin, DeleteView):
	model = Entrenador
	template_name = "entrenador/eliminarE.html"

	def get_success_url(self):
		return reverse_lazy('listaE', kwargs={'modal': 'show'})

class EstadisticasEntrenador(DetailView):
	model = Entrenador
	template_name = "entrenador/estadE.html"

	def get_context_data(self, **kwargs):
		context = super(EstadisticasEntrenador, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk') ###Clave del Entrenador

		tres_mas_ganadores = Caballo.objects.extra(select={ ###3 caballos más ganadores del entrenador
				'nombre': "nombre",
				'cantganados': "select count(*) from jornada_detallescarrera where id_caba_id=caballo_caballo.id and posicion=1"
			}, where={
				"id_entre_id = %s",
				"estatus='a'"
			}, params={pk}).order_by('-cantganados')[:3]

		caballos_entrenador = Caballo.objects.filter(id_entre_id = pk, estatus='a')
		sum_posiciones = 0
		cant = 0

		for caballo in caballos_entrenador:
			query = DetallesCarrera.objects.extra(select={
				'sum': 'sum(posicion)',
				'count': 'count(posicion)'
			}, where={
				'posicion!=500',
				'id_caba_id = %s'
			}, params={caballo.id}
			)[0]
			if query.count!=0 and query != None:
				sum_posiciones += query.sum
			cant += query.count
	
		if (cant!=0):
			context['promedio'] = sum_posiciones/cant
		else:
			context['promedio'] = 0
		context['3masganadores'] = tres_mas_ganadores
		return context