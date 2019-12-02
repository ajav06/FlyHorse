from django.db import models
from django.utils import timezone


class Hipodromo(models.Model):
    nombre = models.CharField(max_length=20)
    rif = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20)
    nombre_dueno = models.CharField(max_length=20)
    fecha_registro = models.DateField(default=timezone.now)
    foto = models.ImageField(upload_to='assets/hipodromos/')

    LOAN_STATUS = (
        ('a', 'Activo'),
        ('e', 'Eliminado'),
    )

    estatus = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    def __str__(self):
        return self.nombre
