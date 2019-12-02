from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', views.IncluirEntrenador.as_view(), name='incluirE'),
    path('listaEntr/<modal>', views.ListaEntrenadores.as_view(), name='listaE'),
    path('actualizarE/<int:pk>/', views.ActualizarEntrenador.as_view(), name='actuE'),
    path('eliminarE/<int:pk>/', views.EliminarEntrenador.as_view(), name='elimE'),
    path('estadE/<int:pk>/', views.EstadisticasEntrenador.as_view(), name='estadE'),
]
