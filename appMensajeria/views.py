from django.shortcuts import render
from .models import *
from .forms import formMensaje, formReceptor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def seleccionarUsuario(request):
    usuarios=User.objects.all
    return render(request, 'appMensajeria/seleccionarUsuario.html', {'users':usuarios})

@login_required
def recibirMensaje(request):

    mensajes=mensaje.objects.filter(receptor=request.user)
    for msj in mensajes:
            msj.leido=True
            msj.save()
       
    return render(request, 'appMensajeria/leerMensajeRecibido.html', {'mensajes':mensajes})

@login_required
def mensajesEnviados(request):

    mensajes=mensaje.objects.filter(emisor=request.user)
    
       
    return mensajes

@login_required
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

            return render(request, 'appMensajeria/enviarMensaje.html', {'mensajes':mensajesEnviados(request)})
    else:
        form=formMensaje()

    return render(request, 'appMensajeria/enviarMensaje.html', {'formulario':form, 'mensajes':mensajesEnviados(request)} )


