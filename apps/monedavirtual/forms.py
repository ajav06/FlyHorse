from django import forms
from .models import MonedaVirtual, Transaccion, Banco


class ActualizarMonedaForm(forms.ModelForm):

    class Meta:
        model = MonedaVirtual

        fields = [
            'precio_bs',
            'precio_divisa',
        ]

class RegistrarTransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            'usua',
            'monto',
            'bco',
            'bco_retiro',
            'ref',
            'descripcion',
            'tipo',
        ]
        widgets = {
            'usua': forms.Select(attrs={'class': 'form-control','value':'{{ user.id }}'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': "any"}), 
            'bco': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'bco_retiro': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'ref': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }

    def clean(self): ## VALIDACION DE MONTO
        cleaned_data = super(RegistrarTransaccionForm, self).clean()
        monto = cleaned_data.get("monto")
        u = cleaned_data.get("usua")
        t = cleaned_data.get("tipo")
        if (float(monto)>u.balance) and (t == 'd'): ##Monto no puede ser mayor al balance, la transaccion debe ser un debito
            raise forms.ValidationError("El monto a retirar no puede ser mayor al balance.", 'monto')
        return cleaned_data


class RegistrarBancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = [
            'bco',
            'usua',
            'numero',
            'tipo',
            'ident',
            'names',
        ]
        widgets = {
            'bco': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'usua': forms.Select(attrs={'class': 'form-control', 'value': '{{ user.id }}'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'ident': forms.TextInput(attrs={'class': 'form-control'}),
            'names': forms.TextInput(attrs={'class': 'form-control'}),
        }
