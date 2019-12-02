from django.db import models
from django.utils import timezone as tezeta
from apps.hipodromo.models import Hipodromo
from apps.jockey.models import Jockey
from apps.caballo.models import Caballo
from datetime import datetime
from pytz import timezone

class JornadaH(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_hip = models.ForeignKey(Hipodromo, on_delete=models.CASCADE)
    fecha = models.DateField(default=tezeta.now)
    cant_carr = models.IntegerField()
    fecha_reg = models.DateField(default=tezeta.now)
    LOAN_STATUS = (
        ('a', 'Activa'),
        ('e', 'Eliminada'),
        ('f', 'Finalizada'),
    )
    estatus = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    def __str__(self):
        return 'Jornada del día: %s. Hipódromo: %s' % (self.fecha, self.id_hip.nombre)

class Carrera(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_jh = models.ForeignKey(JornadaH, on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    cant_caballos = models.IntegerField(null=True)
    distancia = models.FloatField(max_length=4, null=True)
    LOAN_STATUS = (
        ('a', 'Activa'),
        ('c', 'Corriendo'),
        ('f', 'Finalizada'),
        ('e', 'Eliminada'),
        ('p', 'Publicada'),
    )
    estatus = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')
    publicable = models.BooleanField(default=False)

    def __str__(self):
        return 'Hora de la Carrera: %s' % (self.hora)
    
def ActualizarEstatusCarrerasCorriendo(): #APS no permite (aparentemente, según leí en la documentación) enviar parámetros en los métodos.
    #Por eso me toca hacer algo sencillo: buscar todas las jornadas con la fecha de ese momento,
    #todas las carreras que estén comenzando, y actualizar su estatus.
    #OJO: Confío en que todo el proceso no tome más de un minuto o se me enchaba el proceso.
    tz = timezone('America/Caracas')
    print(tz)
    jornadas = JornadaH.objects.filter(fecha=datetime.now(tz).date().strftime("%Y-%m-%d"))
    for jornada in jornadas:
        carreras = Carrera.objects.filter(id_jh_id=jornada.id, hora=datetime.now(tz).time().strftime("%H:%M:00"))
        for carrera in carreras:
            carrera.estatus = 'c'
            carrera.save()
    trabajos = Job.objects.filter(fecha=datetime.now(tz).date().strftime("%Y-%m-%d"),hora=datetime.now(tz).time().strftime("%H:%M:00")) #Obviamente deben actualizarse en la BD, de lo contrario, RIP
    if trabajos:
        for trabajo in trabajos:
            trabajo.estado = 'e'
            trabajo.save()

def ActualizarEstatusCarrerasCorriendoPendientes(f, h): #Si ya comenzaron, actualizo el estatus de forma directa.
    print(f)
    jornadas = JornadaH.objects.filter(fecha=f)
    for jornada in jornadas:
        carreras = Carrera.objects.filter(id_jh_id=jornada.id, hora=h)
        for carrera in carreras:
            carrera.estatus = 'c'
            carrera.save()
    trabajos = Job.objects.filter(fecha=f,hora=h) #Obviamente deben actualizarse en la BD, de lo contrario, RIP
    if trabajos:
        for trabajo in trabajos:
            trabajo.estado = 'e'
            trabajo.save()

class DetallesCarrera(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    id_carr = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_caba = models.ForeignKey(Caballo, on_delete=models.CASCADE)
    id_jock = models.ForeignKey(Jockey, on_delete=models.CASCADE)
    posicion = models.IntegerField(blank=True, null=True)
    LOAN_STATUS = (
        ('a', 'Activa'),
        ('r', 'Retirado'),
    )
    estatus = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')

# class Job(models.Model):
#     fecha = models.DateField(max_length=20, blank=False, null=False)
#     hora = models.TimeField(max_length=10, blank=False, null=False)
#     LOAN_STATUS = (
#         ('p', 'Pendiente'),
#         ('e', 'Ejecutado'),
#     )
#     estado = models.CharField(max_length=1, default='p')