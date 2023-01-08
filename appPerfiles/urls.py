from django.urls import path
from appPerfiles.views import *

urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('editarPerfil/', agregarAvatar, name='agregarAvatar'),
    path('datosPerfil/', datosPerfil, name='datosPerfil'),
    path('editarDatos/', agregarDatosPerfil, name='agregarDatos'),
    
]

