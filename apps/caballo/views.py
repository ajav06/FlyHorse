from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import IncluirCaballoForm, ModificarCaballoForm
from .models import Caballo
from apps.jornada.models import DetallesCarrera
from django.views.generic.list import ListView
from flyhorse.mixin import AuthenticatedAdminMixin
import math

# Create your views here.

class IncluirCaballo(AuthenticatedAdminMixin, CreateView):
	model = Caballo
	form_class = IncluirCaballoForm
	template_name = "caballo/incluirC.html"

	def get_success_url(self):
		return reverse_lazy('incluirC', kwargs={'modal': 'show'})

	def get_context_data(self, **kwargs):
		context = super(IncluirCaballo, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context	


class ListaCaballos(AuthenticatedAdminMixin, ListView):
	model = Caballo
	template_name = "caballo/listaC.html"

	def get_context_data(self, **kwargs):
		context = super(ListaCaballos, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		return context


class ActualizarCaballo(AuthenticatedAdminMixin, UpdateView):
	model = Caballo
	form_class = ModificarCaballoForm
	template_name = "caballo/actualizarC.html"

	def get_success_url(self):
		return reverse_lazy('listaCb', kwargs={'modal': 'show'})

class EliminarCaballo(AuthenticatedAdminMixin, DeleteView):
	model = Caballo
	template_name = "caballo/eliminarC.html"
	
	def get_success_url(self):
		return reverse_lazy('listaCb', kwargs={'modal': 'show'})

class EstadisticasCaballo(DetailView):
	model = Caballo
	template_name = "caballo/estadC.html"

	def get_context_data(self, **kwargs):
		pk = self.kwargs.get('pk')
		context = super(EstadisticasCaballo, self).get_context_data(**kwargs)
		posiciones=''

		### GENERAR CANTIDAD DE VECES QUE HA LLEGADO EN LAS PRIMERAS 5 POSICIONES
		### Realiza un conjunto sucesivo de consultas con sentencias SQL parecidas a la siguiente:
		### SELECT COUNT(id) 
		### AS conteo 
		### FROM jornada_detallescarrera 
		### WHERE posicion = i (i = 1, 2, 3, 4, 5) 
		### AND id_caba_id = id
		### AND estatus='a'
		### Almacena esto en un string que lucirá como el siguiente:
		### 2, 0, 3, 4, 5
		### Y envía eso como parámetro al template, que lo graficará
		for i in range(1,6):
			cant_posi = DetallesCarrera.objects.extra(select={
				'conteo': "COUNT(id)"
			}, where={
				"posicion = "+str(i),
				"estatus = 'a'",
				"id_caba_id = %s"
			}, params={pk})
			for p in cant_posi:
				if i!=5:
					posiciones=posiciones + str(p.conteo) + ', '
				else:
					posiciones=posiciones + str(p.conteo)
		
		###POSICION MEDIA
		###Realiza una sentencia SQL en la que consulta avg(posicion) del caballo en cuestion
		pm = ''
		pos_media = DetallesCarrera.objects.extra(select={
				'media': "AVG(posicion)"
			}, where={
				"estatus = 'a'",
				"id_caba_id = %s",
				"posicion != 500"
			}, params={pk})
		for p in pos_media:
			pm = p.media
		if pm==None:
			pm = 0
		
		pm = str('%.3f'%pm)

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
				"id_caba_id = %s",
				"posicion != 500"
			}, params={pk})

		N = DetallesCarrera.objects.extra(select={ ### (3) cantidad de carreras
				'cant': "COUNT(posicion)"
			}, where={
				"estatus = 'a'",
				"id_caba_id = %s"
			}, params={pk})
		for n in N:
			Nn = int(n.cant)

		sum = 0
		for p in pos:
			if (p.posicion!='' or p.posicion!=None or p.posicion!=500):
				sum = sum + math.pow((int(p.posicion) - float(pm)),2) ###sumatoria
			
		if Nn != 0: ### valido para no dividir entre 0
			desv = math.sqrt(sum / Nn)
		else:
			desv = 0

		desv = '%.3f'%desv
		context['variacion'] = str(desv)
		context['posiciones_lugar'] = posiciones
		context['media'] = pm
		return context