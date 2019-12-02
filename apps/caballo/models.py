from django.db import models
from django.utils import timezone
from apps.entrenador.models import Entrenador
from apps.hipodromo.models import Hipodromo

class Caballo(models.Model):
    id_entre = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    id_hip = models.ForeignKey(Hipodromo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    peso = models.FloatField(max_length=4, null=True)
    fecha_Registro = models.DateField(default=timezone.now, editable=False)
    fecha_nac = models.DateField(default=timezone.now)
    LOAN_STATUS = (
        ('a', 'Activo'),
        ('e', 'Eliminado'),
    )
    foto = models.ImageField(upload_to='assets/caballos/')
    estatus = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    def __str__(self):
        return self.nombre

