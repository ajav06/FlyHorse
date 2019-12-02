from django.db import models
from django.utils import timezone

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nac = models.DateField(default=timezone.now)
    LOAN_STATUS = (
        ('a', 'Activo'),
        ('e', 'Eliminado'),
    )
    estatus = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    def __str__(self):
        return self.nombre

    foto = models.ImageField(upload_to='assets/entrenadores/')
