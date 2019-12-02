from django import forms
from .models import Caballo

class IncluirCaballoForm(forms.ModelForm):

    class Meta:
        model = Caballo

        fields = [
            'id_entre',
            'id_hip',
            'nombre',
            'peso',
            'fecha_nac',
        ]
        widgets={
            'id_entre': forms.Select(attrs={'class': 'form-control'}),
            'id_hip': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step':'any'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control'}),
        }

class ModificarCaballoForm(forms.ModelForm):

    class Meta:
        model = Caballo

        fields = [
            'id_entre',
            'id_hip',
            'nombre',
            'peso',
        ]
        widgets={
            'id_entre': forms.Select(attrs={'class': 'form-control'}),
            'id_hip': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step':'any'}),
        }        


