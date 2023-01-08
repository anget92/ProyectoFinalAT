from django.shortcuts import render
from .models import Avatar, informacionPerfil
from .forms import AvatarForm, agregarInfoPerfil
from . import forms

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


def perfil(request):
    return render(request, 'appPerfiles/perfil.html', {'imagen':obtenerAvatar(request), 'info':datosPerfil(request)})



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


def agregarDatosPerfil(request):
    if request.method=='POST':
        form=agregarInfoPerfil(request.POST)
        if form.is_valid():

            infoVieja=informacionPerfil.objects.filter(user=request.user)

            if len(infoVieja) != 0:
                infoVieja.delete()

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
    return render(request, 'appPerfiles/editarDatos.html', {'form_datos':form})

