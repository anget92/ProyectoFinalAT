from django.shortcuts import render
from .models import Avatar, informacionPerfil
from .forms import AvatarForm, agregarInfoPerfil
from . import forms
from django.contrib.auth.decorators import login_required



def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        imagen=lista[0].imagen.url
    else:
        imagen='/media/avatares/default.webp'
    return imagen


def datosPerfil(request):
    info=informacionPerfil.objects.filter(user=request.user)
    if len(info) != 0:
        datos=info
    else:
        datos={'datos':'Sin datos'}
    return datos

@login_required
def perfil(request):
    return render(request, 'appPerfiles/perfil.html', {'imagen':obtenerAvatar(request), 'info':datosPerfil(request)})


@login_required
def agregarAvatar(request):
    if request.method=='POST':
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo) !=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES['imagen'])
            avatar.save()
            return render(request, 'appPerfiles/perfil.html', {'mensaje': 'Avatar agregado correctamente','imagen':obtenerAvatar(request), 'info':datosPerfil(request)})
        else:
            return render(request, 'appPerfiles/editarPerfil.html', {'form':form, 'usuario':request.user})
    else:
        form=AvatarForm()
    return render(request, 'appPerfiles/editarPerfil.html', {'form':form, 'usuario':request.user})

@login_required
def agregarDatosPerfil(request):
    if request.method=='POST':
        form=agregarInfoPerfil(request.POST)
        if form.is_valid():

            diccionario=form.cleaned_data
            fecha=diccionario['fecha_nacimiento']
            ubicacion=diccionario['ubicacion']
            biografia=diccionario['biografia']
            user=request.user

            datos=informacionPerfil(fecha_nacimiento=fecha, ubicacion=ubicacion, biografia=biografia, user=user)
            
            datos.save()
            return render(request, 'appPerfiles/perfil.html', {'info':datosPerfil(request), 'imagen':obtenerAvatar(request), 'usuario':user})

    else:
        form=agregarInfoPerfil()
    return render(request, 'appPerfiles/agregarDatos.html', {'form':form})

@login_required
def editarDatosPerfil(request):
    datos=informacionPerfil.objects.get(user=request.user)

    if request.method=='POST':
        form=agregarInfoPerfil(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            datos.fecha_nacimiento=informacion['fecha_nacimiento']
            datos.ubicacion=informacion['ubicacion']
            datos.biografia=informacion['biografia']
            datos.save()
            return render(request, 'appPerfiles/perfil.html', {'imagen':obtenerAvatar(request), 'info':datosPerfil(request)} )
    else:
        form=agregarInfoPerfil(initial={'fecha_nacimiento':datos.fecha_nacimiento, 'ubicacion':datos.ubicacion, 'biografia':datos.biografia})
    return render(request, 'appPerfiles/agregarDatos.html', {'form':form, 'datos':datos} )

@login_required
def info_datosPerfil(request):

    info=informacionPerfil.objects.filter(user=request.user)

    if len(info)!=0:
        
        return editarDatosPerfil(request)

    else:
        
        return agregarDatosPerfil(request)

    
        
    