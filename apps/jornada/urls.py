from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<modal>', views.IncluirJornada.as_view(), name='incluirJh'),
    path('carrera/', views.IncluirCarrera.as_view(), name='incluirCr'),
    path('listaJorh/<modal>', views.ListaJornada.as_view(), name='listaJh'),
    path('actualizarJh/<pk>/', views.ActualizarJornada.as_view(), name='actuJh'),
    path('eliminarJh/<pk>/', views.EliminarJornada.as_view(), name='elimJh'),
    path('consultarJh/<pk>/<modal>', views.ConsultarJornada.as_view(), name='consJh'),
    path('listaCarr/', views.ListaCarrera.as_view(), name='listaCr'),
    path('actualizarCr/<pk>/', views.ActualizarCarrera.as_view(), name='actuCr'),
    path('finalizarCr/<pk>/', views.FinalizarCarrera.as_view(), name='finalCr'),
    path('eliminarCr/<pk>/', views.EliminarCarrera.as_view(), name='elimCr'),
    path('listaCarr/<pk>/detalleC/<modal>', views.ListaDetallesC.as_view(), name='detalleC'),
    path('listaCarr/<pk>/detalleC/<modal>/agregar', views.RegistrarDetalles.as_view(), name='RegDetallCr'),
    path('listaCarr/<pk>/detalleC/<modal>/mod', views.ActualizarDetalle.as_view(), name= 'actuDetall'),
    path('listaCarr/<pk>/detalleC/<modal>/elim', views.RetirarCompetidor.as_view(), name= 'elimDetall'),
    path('listaCarrJor/<pk>/detalleC', views.ListaDetallesCarrJ.as_view(), name='detalleCJ'),
    path('listaCarrJor/<pk>/detalleC/resultado', views.RegistrarResultados.as_view(), name='RegResultCr'),
    path('publicar/<pk>/', views.PublicarResultados.as_view(), name='PubResultadosCr'),
    path('listadoCarreras/',views.listadoCarreras.as_view(), name='listC'),
    path('ConsultarC/<pk>/',views.ConsultarC.as_view(), name='ConsulC'),
]
