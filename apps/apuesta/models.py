from django.db import models
from apps.usuario.models import User
from django.utils import timezone
from apps.caballo.models import Caballo
from apps.jornada.models import Carrera, JornadaH
from apps.monedavirtual.models import Transaccion


class TipoApuesta(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=70)
    estatus = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.nombre

class Apuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tApuesta = models.ForeignKey(TipoApuesta, on_delete=models.CASCADE, blank=True, null=True)
    id_carr = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True, null=True)
    id_jorh = models.ForeignKey(JornadaH, on_delete=models.CASCADE, blank=True, null=True)
    cuota = models.FloatField(max_length=4, blank=True, null=True)
    fechaAp = models.DateField(default=timezone.now)
    idTrans = models.ForeignKey(Transaccion, on_delete=models.CASCADE, blank = True, null = True, related_name='trans_apuesta')
    idTransGanada = models.ForeignKey(Transaccion, on_delete=models.CASCADE, blank = True, null = True, related_name='trans_ganadora')
    LOAN_STATE = (
        ('A','Activa'),
        ('G','Ganada'),
        ('P','Perdida'),
        ('D','Devuelta'),
    )
    estatus = models.CharField(max_length=1, default='A', choices=LOAN_STATE)

class DetalleApuesta(models.Model):
    id_ap = models.ForeignKey(Apuesta, on_delete=models.CASCADE, blank=True, null=True)
    id_cab = models.ForeignKey(Caballo, on_delete=models.CASCADE, blank=True, null=True)
    posicion = models.IntegerField(blank=True, null=True)
    montoD = models.FloatField(max_length=10, blank=True, null=True)
