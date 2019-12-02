from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Type_User(models.Model):
    codigo = models.CharField(max_length=8, primary_key=True)
    tipo_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class User(AbstractUser):
    city = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    balance = models.FloatField(default=0)
    type_u = models.ForeignKey(Type_User, on_delete=models.CASCADE, blank=True, null=True, default = 'user')
    last_access = models.DateTimeField(default=timezone.now)

    def incrementarSaldo(self, incremento, nomusu):
        usua = User.objects.get(username=nomusu)
        usua.balance += incremento
        usua.save()
    
    def disminuirSaldo(self, decremento, nomusu):
        usua = User.objects.get(username=nomusu)
        if decremento <= usua.balance:
            usua.balance -= decremento
            usua.save()
            return True
        return False
