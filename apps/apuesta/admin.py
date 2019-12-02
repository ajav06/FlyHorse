from django.contrib import admin
from .models import Apuesta, DetalleApuesta, TipoApuesta
# Register your models here.
admin.site.register(Apuesta)
admin.site.register(DetalleApuesta)
admin.site.register(TipoApuesta)
