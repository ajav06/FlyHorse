from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IncluirHipodromoForm
from .models import Hipodromo
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from flyhorse.mixin import AuthenticatedAdminMixin
from apps.jornada.models import *
# Create your views here.


class IncluirHipo(AuthenticatedAdminMixin, CreateView):
	model = Hipodromo
	form_class = IncluirHipodromoForm
	template_name = "hipodromo/incluirH.html"

	def get_success_url(self):
		return reverse_lazy('incluirH', kwargs={'modal': 'show'})

	def get_context_data(self, **kwargs):
		context = super(IncluirHipo, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context

class ListaHipodromos(AuthenticatedAdminMixin, ListView):
	model = Hipodromo
	template_name = "hipodromo/listaH.html"

	def get_context_data(self, **kwargs):
		context = super(ListaHipodromos, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context

class ActualizarHipo(AuthenticatedAdminMixin, UpdateView):
	model = Hipodromo
	form_class = IncluirHipodromoForm
	template_name = "hipodromo/actualizarH.html"
	
	def get_success_url(self):
		return reverse_lazy('listaH', kwargs={'modal': 'show'})

class EliminarHipodromo(AuthenticatedAdminMixin, DeleteView):
	model = Hipodromo
	template_name = "hipodromo/eliminarH.html"
	
	def get_success_url(self):
		return reverse_lazy('listaH', kwargs={'modal': 'show'})

class EstadisticasHipodromo(DetailView):
	model = Hipodromo
	template_name = "hipodromo/estadH.html"

	def get_context_data(self, **kwargs):
		context = super(EstadisticasHipodromo, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk') ###Clave del Hipodromo

		ult_jornada = JornadaH.objects.filter(id_hip_id=pk).order_by('-fecha')[0] ###Busco cuál fue la última jornada del hipodromo
		ult_6carr = Carrera.objects.filter(id_jh_id=ult_jornada.id,estatus='p').order_by('-hora')[:6] ###Busco las últimas 6 carreras del hipódromo
		ganadores = []
		for carr in ult_6carr:
			ganadores.append(DetallesCarrera.objects.filter(id_carr_id = carr.id).order_by('posicion')[0]) ###Guardo el ganador de cada una de las últimas 6 carreras
		
		promedio = JornadaH.objects.extra(select={ ###Promedio de carreras de un hipódromo por jornada
				'promedio': "AVG(cant_carr)"
			}, where={
				"id_hip_id = %s",
			}, params={pk})[0].promedio
		
		##Más ganadores, segundones, tercerones, cuartones

		mas_ganador = Caballo.objects.extra(select={ ###Promedio de carreras de un hipódromo por jornada
				'nombre': "nombre",
				'cantidad': "select count(*) from jornada_detallescarrera where id_caba_id = caballo_caballo.id and posicion = 1"
			}, where={
				"id_hip_id = %s",
			}, params={pk}).order_by('-cantidad')[0]

		mas_segundo = Caballo.objects.extra(select={ ###Promedio de carreras de un hipódromo por jornada
				'nombre': "nombre",
				'cantidad': "select count(*) from jornada_detallescarrera where id_caba_id = caballo_caballo.id and posicion = 2"
			}, where={
				"id_hip_id = %s",
			}, params={pk}).order_by('-cantidad')[0]

		mas_tercero = Caballo.objects.extra(select={ ###Promedio de carreras de un hipódromo por jornada
				'nombre': "nombre",
				'cantidad': "select count(*) from jornada_detallescarrera where id_caba_id = caballo_caballo.id and posicion = 3"
			}, where={
				"id_hip_id = %s",
			}, params={pk}).order_by('-cantidad')[0]	

		mas_cuarto = Caballo.objects.extra(select={ ###Promedio de carreras de un hipódromo por jornada
				'nombre': "nombre",
				'cantidad': "select count(*) from jornada_detallescarrera where id_caba_id = caballo_caballo.id and posicion = 4"
			}, where={
				"id_hip_id = %s",
			}, params={pk}).order_by('-cantidad')[0]	

		context['mas_ganador'] = mas_ganador
		context['mas_segundo'] = mas_segundo
		context['mas_tercero'] = mas_tercero
		context['mas_cuarto'] = mas_cuarto
		context['ganadores'] = ganadores
		context['promedio'] = str('%.2f'%promedio).replace('.', ',')
		return context