from django.shortcuts import render
from .models import *
from .forms import formMensaje, formReceptor
from django.contrib.auth.models import User

def seleccionarUsuario(request):
    usuarios=User.objects.all
    return render(request, 'appMensajeria/seleccionarUsuario.html', {'users':usuarios})


def enviarMensaje(request):
    usuarios=User.objects.all
    if request.method=='POST':
        
        form=formMensaje(request.POST)
        if form.is_valid():
            diccionario=form.cleaned_data
            cuerpo=diccionario['cuerpo']
            emisor=request.user
            receptor=User.objects.get(username=diccionario['receptor'])
            formulario=mensaje(emisor=emisor, cuerpo=cuerpo, receptor=receptor)
            formulario.save()

            return render(request, 'appPerfiles/Perfil.html', {'formulario':formulario, 'users':usuarios, 'mensaje':'Enviaste el mensaje'})
    else:
        form=formMensaje()

    return render(request, 'appMensajeria/enviarMensaje.html', {'formulario':form} )

def recibirMensaje(request):

    mensajes=mensaje.objects.filter(receptor=request.user)
    for msj in mensajes:
            msj.leido=True
            msj.save()
       
    return render(request, 'appMensajeria/leerMensajeRecibido.html', {'mensajes':mensajes})

# def leerMensajeUsuario(request):
#     return render(request, 'appMensajeria/leerMensaje.html')

# def leerMensajes(request):
#     if request.GET['receptor']:
#         user=request.GET['receptor']
        
#         mensajes=mensaje.objects.filter(receptor=request.user)
#         return render(request, 'appMensajeria/leerMensajeRecibido.html', {'mensajes':mensajes})
#     else:
#         return render(request, 'appMensajeria/leerMensajeRecibido.html')