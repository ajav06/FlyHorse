from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import MonedaVirtual, Transaccion
from .forms import ActualizarMonedaForm, RegistrarTransaccionForm
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
import datetime
from flyhorse.mixin import AuthenticatedAdminMixin
# Create your views here.

class ActualizarPrecio(AuthenticatedAdminMixin, CreateView):
	model = MonedaVirtual
	form_class = ActualizarMonedaForm
	template_name = "administrador/actualizarM.html"

	def get_success_url(self):
		return reverse_lazy('histMv', kwargs={'modal': 'show'})


class HitorialM(AuthenticatedAdminMixin, ListView):
	model = MonedaVirtual
	template_name = "administrador/historialM.html"
	ordering = ['-fecha']

		
	def get_context_data(self, **kwargs):
		context = super(HitorialM, self).get_context_data(**kwargs)
		context['show'] = self.kwargs.get('modal')
		context['object_list'] = MonedaVirtual.objects.all()
	

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
		
		context['hoy'] = ano + '-' + mes + '-' + dia
		return context
