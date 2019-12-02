from django import forms
from .models import Hipodromo


class IncluirHipodromoForm(forms.ModelForm):

    class Meta:
        model = Hipodromo

        fields = [
            'nombre',
            'rif',
            'estado',
            'ciudad',
            'telefono',
            'nombre_dueno',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rif': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_dueno': forms.TextInput(attrs={'class': 'form-control'}),
        }
