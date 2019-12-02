from django import forms
from .models import Apuesta, DetalleApuesta
from apps.monedavirtual.models import Transaccion
from betterforms.multiform import MultiForm, MultiModelForm
from betterforms.forms import BetterForm
from apps.usuario.models import User
class RegistrarTransApuForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            'usua', #
            'monto', #
            'descripcion', #
            'tipo', #
            'estado',
        ]
        widgets = {
            'usua': forms.TextInput(attrs={'class': 'form-control', 'value': "{{ user.id }}"}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': "any",'placeholder':"Monto"}),
            'descripcion': forms.NumberInput(attrs={'class': 'form-control', 'step': "any", 'value':30}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'value': "d"}),
        }

    def clean(self):  # VALIDACION DE MONTO
        cleaned_data = super(RegistrarTransApuForm, self).clean()
        print(cleaned_data)
        monto = cleaned_data.get("monto")
        u = cleaned_data.get("usua")
        t = cleaned_data.get("tipo")
        # Monto no puede ser mayor al balance, la transaccion debe ser un debito
        if (float(monto) > u.balance) and (t == 'd'):
            raise forms.ValidationError(
                "El monto a Apostar no puede ser mayor al balance.", 'monto')
        return cleaned_data

class RegistrarDetaApuFrom(forms.ModelForm):
    class Meta:
        model = DetalleApuesta
        fields = [
            'id_cab', #
            'posicion', #
        ]
        widgets = {
            'id_cab': forms.Select(attrs={'class': 'form-control', 'value': "{{ caballo }}" }),
            'posicion': forms.NumberInput(attrs={'class': 'form-control','placeholder':"Posición"}),
        }

class RegistrarDetaApuFrom2(forms.ModelForm):
    class Meta:
        model = DetalleApuesta
        fields = [
            'id_cab', #
            'posicion', #
        ]
        widgets = {
            'id_cab': forms.Select(attrs={'class': 'form-control', 'value': "{{ caballo }}" }),
            'posicion': forms.NumberInput(attrs={'class': 'form-control','placeholder':"Posición"}),
        }

class RegistrarApuFrom(forms.ModelForm):
    class Meta:
        model = Apuesta
        fields = [
            'tApuesta', #
            'id_carr', #
            'cuota', #
            'id_jorh',
        ]
        widgets = {
            'tApuesta': forms.TextInput(attrs={'class': 'form-control', 'value': "{{ tipoap.id }}"}),
            'id_carr': forms.TextInput(attrs={'class': 'form-control', 'value': "{{ carreras.id }}"}),
            'id_jorh': forms.TextInput(attrs={'class': 'form-control'}),
            'cuota': forms.TextInput(attrs={'class': 'form-control', 'step': "any", 'value':'10','placeholder':"Cuota",'name':"apue-cuota"}),
        }
   
class MultiplesForm(MultiModelForm):
    form_classes = {
        'trans': RegistrarTransApuForm,
        'apue': RegistrarApuFrom,
        'detaAp': RegistrarDetaApuFrom,
        'detaAp2': RegistrarDetaApuFrom,
        'detaAp3': RegistrarDetaApuFrom, 
        'detaAp4': RegistrarDetaApuFrom,  
    }
    fieldsets =(('detaAp',{'fields':('id_cab','posicion')}),
                ('detaAp2',{'fields':('id_cab','posicion')}),
                ('detaAp3',{'fields':('id_cab','posicion')}),
                ('detaAp4',{'fields':('id_cab','posicion')}),
                ('trans',{'fields':('usua','monto','descripcion','tipo','estado')}),
                ('apue',{'fields':('tApuesta','id_carr','cuota')}),)
   
MultiplesForm(initial={
    'trans':{
        'usua':'{{ user.id }}', 
        'monto':'10', 
        'descripcion':'30', 
        'tipo':'d',
        'estado':'c', 
    },
    'apue':{
        'tApuesta':'{{ tP }}',
        'id_carr':'{{ carr }}',
        'cuota':'{{ cuota }}'
    },
    'detaAp':{
        'id_cab':'{{ caballo }}', 
        'posicion':'1', 
    },
})


class MultiplesForm5y6(MultiModelForm):
    form_classes = {
        'trans': RegistrarTransApuForm,
        'apue': RegistrarApuFrom,
        'detaAp1': RegistrarDetaApuFrom,
        'detaAp2': RegistrarDetaApuFrom,
        'detaAp3': RegistrarDetaApuFrom,
        'detaAp4': RegistrarDetaApuFrom,
        'detaAp5': RegistrarDetaApuFrom,
        'detaAp6': RegistrarDetaApuFrom,
        'detaAp7': RegistrarDetaApuFrom,
        'detaAp21': RegistrarDetaApuFrom,
        'detaAp22': RegistrarDetaApuFrom,
        'detaAp23': RegistrarDetaApuFrom,
        'detaAp24': RegistrarDetaApuFrom,
        'detaAp25': RegistrarDetaApuFrom,
        'detaAp26': RegistrarDetaApuFrom,
        'detaAp27': RegistrarDetaApuFrom,
    }
    fieldsets = (('detaAp1', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp2', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp3', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp4', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp5', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp6', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp7', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp21', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp22', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp23', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp24', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp25', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp26', {'fields': ('id_cab', 'posicion')}),
                 ('detaAp27', {'fields': ('id_cab', 'posicion')}),
                 ('trans', {'fields': ('usua', 'monto','descripcion', 'tipo', 'estado')}),
                 ('apue', {'fields': ('tApuesta', 'cuota', 'id_jorh')}),)
