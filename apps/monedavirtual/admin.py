from django.contrib import admin
from .models import MonedaVirtual, Transaccion, Banco
# Register your models here.
admin.site.register(MonedaVirtual)
admin.site.register(Transaccion)
admin.site.register(Banco)
