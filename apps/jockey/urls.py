from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', views.IncluirJockey.as_view(), name='incluirJk'),
    path('listaJock/<modal>', views.ListaJockeys.as_view(), name='listaJk'),
    path('actualizarJk/<int:pk>/', views.ActualizarJockey.as_view(), name='actuJk'),
    path('eliminarJk/<int:pk>/', views.EliminarJockey.as_view(), name='elimJk'),
    path('estadisticasJk/<int:pk>/', views.EstadisticasJockey.as_view(), name='estadJk'),
]

 
