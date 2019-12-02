from django import forms
from .models import Carrera, JornadaH, DetallesCarrera, ActualizarEstatusCarrerasCorriendo

class IncluirJornadaForm(forms.ModelForm):

    class Meta:
        model = JornadaH

        fields = [
            'id',
            'id_hip',
            'fecha',
            'cant_carr',
        ]

        widgets={
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'id_hip': forms.Select(attrs={'class': 'form-control', 'id':'uno'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'cant_carr': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ActualizarJornadaForm(forms.ModelForm):

    class Meta:
        model = JornadaH

        fields = [
            'cant_carr',
        ]
        widgets = {
            'cant_carr': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class IncluirCarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera

        fields = [
            'id',
            'id_jh',
            'hora',
            'cant_caballos',
            'distancia',
        ]
        widgets={
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'id_jh': forms.Select(attrs={'class': 'form-control','id':'uno'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'cant_caballos': forms.NumberInput(attrs={'class': 'form-control'}),
            'distancia': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    

class ActualizarCarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera

        fields = [
            'cant_caballos',
            'distancia',
        ]
        widgets = {
            'cant_caballos': forms.NumberInput(attrs={'class': 'form-control'}),
            'distancia': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FinalizarCarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera

        fields = [
            'estatus',
        ]
        widgets = {
            'estatus': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistrarDetallesForm(forms.ModelForm):

    class Meta:
        model = DetallesCarrera

        fields = [
            'id',
            'numero',
            'id_carr',
            'id_caba',
            'id_jock',
        ]

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_carr': forms.Select(attrs={'class': 'form-control','id':'uno'}),
            'id_caba': forms.Select(attrs={'class': 'form-control','id':'dos'}),
            'id_jock': forms.Select(attrs={'class': 'form-control','id':'tres'}),
        }
   
class ActualizarDetallesForm(forms.ModelForm):

    class Meta:
        model = DetallesCarrera

        fields = [
            'numero',
            'id_caba',
            'id_jock',
        ]
        widgets = {
            'numero' : forms.NumberInput(attrs={'class': 'form-control'}),
            'id_caba': forms.Select(attrs={'class': 'form-control'}),
            'id_jock': forms.Select(attrs={'class': 'form-control'}),
        }

class FinalizarDetallesForm(forms.ModelForm):

    class Meta:
        model = DetallesCarrera

        fields = [
            'estatus',
        ]
        widgets = {
            'estatus': forms.TextInput(attrs={'class': 'form-control'}),
        }        

class RegistrarResultadosForm(forms.ModelForm):
    class Meta:
        model = DetallesCarrera

        fields = [
            'posicion',
        ]
        widgets = {
           'posicion': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ListaCarreraForm(forms.Form):
    estatus=forms.CharField()
