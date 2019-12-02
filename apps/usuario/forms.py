from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from apps.monedavirtual.models import Transaccion
import datetime
from django.utils import timezone

class RegistrarForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class ActualizarFrom(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'city',
            'location',
            'birth_date',
            'phone',
            'email',
        ]


class ActualizarNivelFrom(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'type_u',
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': True}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'type_u': forms.Select(attrs={'class': 'form-control'}),
        }

class SuspenderUsuarioForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'type_u',
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': True}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'type_u': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['type_u'].disabled = True

class GestionarTransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion

        fields = [
            'usua',
            'fecha',
            'bco',
            'ref',
            'bco_retiro',
            'descripcion',
            'monto',
            'tipo',
            'estado',
        ]
        widgets={
            'usua': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'bco': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'bco_retiro': forms.Textarea(attrs={'class': 'form-control', 'readonly': True}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'ref': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-contol', 'readonly': True}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].disabled = True
        self.fields['usua'].disabled = True
        self.fields['monto'].disabled = True
        self.fields['tipo'].disabled = True
        self.fields['bco'].disabled = True
        self.fields['descripcion'].disabled = True
    
    def clean(self): ## VALIDACION DE MONTO
        cleaned_data = super(GestionarTransaccionForm, self).clean()
        monto = cleaned_data.get("monto")
        u = cleaned_data.get("usua")
        t = cleaned_data.get("tipo")
        e = cleaned_data.get("estado")
        if (float(monto)>u.balance) and (t == 'd') and (e == 'a'): ##Monto no puede ser mayor al balance, la transaccion debe ser un debito, el estatus que estoy poniendo debe ser aprobado
            raise forms.ValidationError("El monto a retirar no puede ser mayor al balance.", 'monto')
        return cleaned_data


class ConsultarTransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion

        fields = [
            'usua',
            'fecha',
            'bco',
            'ref',
            'monto',
            'tipo',
            'estado',
        ]
        widgets={
            'usua': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'bco': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'ref': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'monto': forms.TextInput(attrs={'class': 'form-contol', 'readonly': True}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ref'].disabled = True
        self.fields['fecha'].disabled = True
        self.fields['usua'].disabled = True
        self.fields['monto'].disabled = True
        self.fields['tipo'].disabled = True
        self.fields['bco'].disabled = True
        self.fields['estado'].disabled = True
