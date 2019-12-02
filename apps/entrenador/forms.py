from django import forms
from .models import Entrenador


class IncluirEntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador

        fields = [
            'nombre',
            'fecha_nac',
        ]
        wigts={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac':forms.DateInput(attrs={'class': 'form-control'}),
        }

class ModicarEntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador

        fields = [
            'nombre',
        ]
        wigts={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EliminarEntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador

        fields = [
            'estatus',
        ]
        wigts={
            'estatus': forms.TextInput(attrs={'class': 'form-control'}),
        }        

