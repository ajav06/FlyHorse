from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('actualizar/', views.ActualizarPrecio.as_view(), name='monedaV'),
    path('historialM/<modal>', views.HitorialM.as_view(), name='histMv'),
]
