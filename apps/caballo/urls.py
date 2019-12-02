from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', login_required(views.IncluirCaballo.as_view()), name='incluirC'),
    path('listaC/<modal>', login_required(views.ListaCaballos.as_view()), name='listaCb'),
    path('actualizarCb/<int:pk>/', login_required(views.ActualizarCaballo.as_view()), name='actuCb'),
    path('eliminarCb/<int:pk>/', login_required(views.EliminarCaballo.as_view()), name='elimCb'),
    path('estadisticasCb/<int:pk>/', login_required(views.EstadisticasCaballo.as_view()), name='estadCb'),
]
