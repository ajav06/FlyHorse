from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.views import (LogoutView, PasswordResetDoneView, PasswordResetView, 
PasswordResetConfirmView, PasswordResetCompleteView)
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.IniciarSesion.as_view(), name='index'),
    path('signIn/',views.RegistrarUsuario.as_view(),name='signIn'),
    path('logout/', views.CerrarSesion.as_view(), name='logout'),
    path('reset/', PasswordResetView.as_view(), name='reset'),
    path('resetDone/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetConfirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetComplete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('inicio/', views.Inicio.as_view(), name='inicio'),
    path('incluir/', views.Incluir.as_view(), name='incluir'),
    path('gestionar/', views.Gestionar.as_view(), name='gestionar'),
    path('listaUser/<modal>', views.ListaUsuarios.as_view(), name='listaU'),
    path('modificarUser/<pk>/', views.ModificarUser.as_view(), name='actuNu'),
    path('estadistica/', views.Estadistica.as_view(), name='estadistica'),
    path('consultar/', views.Consultar.as_view(),name='consulta'),
    path('configurar/', views.Configuraciones.as_view(), name='configuraciones'),
    path('actualizarUser/<pk>/', views.ActualizarUser.as_view(), name='datosP'),
    path('transManager/pendientes/', views.TransaccionesPendientes.as_view(), name='transPendientes'),
    path('transManager/aprobadas/', views.TransaccionesAprobadas.as_view(), name='transAprobadas'),
    path('transManager/rechazadas/', views.TransaccionesRechazadas.as_view(), name='transRechazadas'),
    path('gestionarTrans/<int:pk>/', views.GestionarTransaccion.as_view(), name='gestionTrans'),
    path('consultarTrans/<int:pk>/', views.ConsultarTransaccion.as_view(), name='consulTrans'),
    path('consultarTransU/<int:pk>/', views.ConsultarTransaccionUsuario.as_view(), name='consulTransUsu'),
    path('saldo/', views.Saldo.as_view(), name='saldo'),
    path('transacciones/<modal>', views.Transacciones.as_view(), name='trans'),
    path('recargar/', views.RegistrarTransD.as_view(), name='recar'),
    path('listaB/', views.ListaBanco.as_view(), name='listB'),
    path('registrarB/', views.RegistrarBanco.as_view(), name='regisB'),
    path('modificarB/<int:pk>/', views.ModificarBanco.as_view(), name='modiB'),
    path('retirar/', views.RegistrarTransC.as_view(), name='retir'),
    path('reglamento/', views.Reglamento.as_view(), name='reglam'),
    path('signInDone/', views.signInDone, name='signIn_done'),
    path('suspenderUsuario/<int:pk>',views.SuspenderUsuario.as_view(), name='susp'),
    path('estadisticasRS', views.EstadisticasRS.as_view(), name='estadRS')
]
