from . import views
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', views.Apostar.as_view(), name='apostar'),
    path('<int:pk>/', views.SelecTipoApuesta.as_view(), name='selecTipoApuesta'),
    path('<pk>/Apuesta_Unicarrera/<ap>', views.Apuesta_Unicarrera.as_view(), name='Apuesta_Unicarrera'),
    path('<pk>/Apuesta_Unicarrera/<ap>/<carr>/Ganador', views.Apuesta_Ganador.as_view(), name='Apuesta_Ganador'),
    path('<pk>/Apuesta_Unicarrera/<ap>/<carr>/Exacta', views.Apuesta_Exacta.as_view(), name='Apuesta_Exacta'),
    path('<pk>/Apuesta_Unicarrera/<ap>/<carr>/Trifecta', views.Apuesta_Trifecta.as_view(), name='Apuesta_Trifecta'),
    path('<pk>/Apuesta_Unicarrera/<ap>/<carr>/Superfecta', views.Apuesta_Superfecta.as_view(), name='Apuesta_Superfecta'),
    path('<pk>/<ap>/Ap5y6', views.Apuesta_5y6.as_view(), name='AP56'),
    path('<pk>/Apuesta_Loto', views.Apuesta_Loto.as_view(), name='Apuesta_Loto'),
    path('<pk>/<ap>/Apuesta_Polla', views.Apuesta_Polla.as_view(), name='Apuesta_Polla'),
    path('ConsultarAP/<pk>/', views.ConsultarAp.as_view(), name='ConsultarAp'),
    path('ListadoApuestas/',views.listadoApuestas.as_view(), name='listA'),
    path('Apostar/<pk>/DetallesCarrera/', views.ListaDetCarr.as_view(), name='listComp'),
    path('<pk>/<ap>/<carr>/Apuesta_Place', views.Apuesta_Place.as_view(), name='Apuesta_Place'),
    path('<pk>/<ap>/<carr>/Apuesta_Show', views.Apuesta_Show.as_view(), name='Apuesta_Show'),
    path('EstadisticasAp/',views.EstadisticasApuesta.as_view(), name='estadAp'),
    path('<pk>/DetallesCarrera/', views.ListaDetCarr.as_view(), name='listComp'),
    path('confirmar/<carr>/<tp>/<cab>', views.Apuesta_Ganador_Confirmar.as_view(), name='ApGanadorConfir'),
]
