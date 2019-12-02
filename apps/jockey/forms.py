from django import forms
from .models import Jockey


class IncluirJockeyForm(forms.ModelForm):

    class Meta:
        model = Jockey

        fields = [
            'nombre',
            'peso',
            'fecha_nac',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step':"any"}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control'}),
        }

class ModificarJockeyForm(forms.ModelForm):

    class Meta:
        model = Jockey

        fields = [
            'nombre',
            'peso',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step':"any"}),
        }

class EliminarEntrenadorForm(forms.ModelForm):

    class Meta:
        model = Jockey

        fields = [
            'estatus',
        ]
        widgets = {
            'estatus': forms.NumberInput(attrs={'class': 'form-control', 'step':"any"}),
        }