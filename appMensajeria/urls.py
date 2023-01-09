from django.urls import path
from appMensajeria.views import *

urlpatterns = [
    path('enviarMensaje/', enviarMensaje, name='enviarMensaje'),
    path('seleccionarUsuario/', seleccionarUsuario, name='seleccionarUsuario'),
    # path('leerMensajeUser/', leerMensajeUsuario, name='leerMensajeUser'),
    # path('leerMensaje/', leerMensajes, name='leerMensaje'),
    path('leerMensajeRecibido', recibirMensaje, name='mensajeRecibido')
]

