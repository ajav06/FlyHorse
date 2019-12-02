from django.db import models
from django.utils import timezone
from apps.usuario.models import User
# Create your models here.

class MonedaVirtual(models.Model):
    fecha = models.DateField(default=timezone.now, primary_key=True)
    precio_bs = models.FloatField(max_length=50)
    precio_divisa = models.FloatField(max_length=10)


class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    usua = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    TYPE_BANCO = (
        ('0156','100%BANCO'),
        ('0196','ABN AMRO BANK'),
        ('0172','BANCAMIGA BANCO MICROFINANCIERO, C.A.'),
        ('0171','BANCO ACTIVO BANCO COMERCIAL, C.A.'),
        ('0166','BANCO AGRICOLA'),
        ('0175','BANCO BICENTENARIO'),
        ('0128','BANCO CARONI, C.A. BANCO UNIVERSAL'),
        ('0164','BANCO DE DESARROLLO DEL MICROEMPRESARIO'),
        ('0102','BANCO DE VENEZUELA S.A.I.C.A.'),
        ('0114','BANCO DEL CARIBE C.A.'),
        ('0149','BANCO DEL PUEBLO SOBERANO C.A.'),
        ('0163','BANCO DEL TESORO'),
        ('0176','BANCO ESPIRITO SANTO, S.A.'),
        ('0115','BANCO EXTERIOR C.A.'),
        ('0003','BANCO INDUSTRIAL DE VENEZUELA.'),
        ('0173','BANCO INTERNACIONAL DE DESARROLLO, C.A.'),
        ('0105','BANCO MERCANTIL C.A.'),
        ('0191','BANCO NACIONAL DE CREDITO'),
        ('0116','BANCO OCCIDENTAL DE DESCUENTO.'),
        ('0138','BANCO PLAZA'),
        ('0108','BANCO PROVINCIAL BBVA'),
        ('0104','BANCO VENEZOLANO DE CREDITO S.A.'),
        ('0168','BANCRECER S.A. BANCO DE DESARROLLO'),
        ('0134','BANESCO BANCO UNIVERSAL'),  
        ('0177','BANFANB'),
        ('0146','BANGENTE'),
        ('0174','BANPLUS BANCO COMERCIAL C.A'),
        ('0190','CITIBANK.'),
        ('0121','CORP BANCA.'),
        ('0157','DELSUR BANCO UNIVERSAL'),
        ('0151','FONDO COMUN'),
        ('0601','INSTITUTO MUNICIPAL DE CR&#201;DITO POPULAR'),
        ('0169','MIBANCO BANCO DE DESARROLLO, C.A.'),
        ('0137','SOFITASA'),
        ('BOFA','BANK OF AMERICA'),
        ('WF','WELLS FARGO'),
        ('ZL','ZELLE')
    )
    bco = models.CharField(max_length=4, choices=TYPE_BANCO, blank=True)
    numero = models.CharField(blank=True, null=True, max_length=20)
    TYPE_CTA = (
        ('c', 'Corriente'),
        ('a', 'Ahorro'),
        ('e', 'Cuenta Extranjera'),
    )
    tipo = models.CharField(max_length=1, choices=TYPE_CTA)
    ident = models.CharField(max_length=20, blank=True, null=True)
    names = models.CharField(max_length=50, blank=True, null=True)

class Transaccion(models.Model):
    usua = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    monto = models.FloatField(max_length=50)
    TYPE_TRANS = (
        ('d', 'Débito'),
        ('c', 'Crédito'),
    )
    tipo = models.CharField(max_length=1, choices=TYPE_TRANS)
    LOAN_STATUS = (
        ('a', 'Aprobada'),
        ('e', 'Pendiente'),
        ('r', 'Rechazada'),
        ('c', 'Completada')
    )
    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='e')
    TYPE_BANCO = (
        ('0108', 'BANCO PROVINCIAL BBVA'),
        ('0116','BANCO OCCIDENTAL DE DESCUENTO.'),
        ('0105','BANCO MERCANTIL C.A.'),
        ('BOFA','BANK OF AMERICA'),
        ('WF','WELLS FARGO'),
        ('ZL','ZELLE')
    )
    bco = models.CharField(max_length=4, choices=TYPE_BANCO, blank=True)
    bco_retiro = models.ForeignKey(Banco, on_delete=models.CASCADE, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True, default=None)
    DESC = (
        (1,'Recarga de Saldo'),
        (2,'Retiro de Saldo'),
        (3,'Apuesta Realizada'),
        (4,'Apuesta Ganada'),
        (5,'Devolución de Apuesta'),    
    )
    descripcion = models.IntegerField(choices=DESC,blank=False,default=1)