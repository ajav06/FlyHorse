from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', views.IncluirHipo.as_view(), name='incluirH'),
    path('listaHipo/<modal>', views.ListaHipodromos.as_view(), name='listaH'),
    path('actualizarH/<int:pk>/', views.ActualizarHipo.as_view(), name='actuH'),
    path('eliminarH/<int:pk>/', views.EliminarHipodromo.as_view(), name='elimH'),
    path('estadisticasH/<int:pk>/', views.EstadisticasHipodromo.as_view(), name='estadH')
]
