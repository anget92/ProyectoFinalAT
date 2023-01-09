from django.urls import path
from appMensajeria.views import *

urlpatterns = [
    path('enviarMensaje/', enviarMensaje, name='enviarMensaje'),
    path('seleccionarUsuario/', seleccionarUsuario, name='seleccionarUsuario'),
    path('recibirMensaje/', recibirMensaje, name='recibirMensaje'),
    path('enviarMensaje/', mensajesEnviados, name='mensajeRecibido')
]

