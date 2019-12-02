from django.db import models
from django.utils import timezone


class Jockey(models.Model):
    nombre = models.CharField(max_length=30)
    peso = models.FloatField(max_length=4)
    fecha_nac = models.DateField()
    LOAN_STATUS = (
        ('a', 'Activo'),
        ('e', 'Eliminado'),
    )
    estatus = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    def __str__(self):
        return self.nombre

    foto = models.ImageField(upload_to='assets/jockeys/')
