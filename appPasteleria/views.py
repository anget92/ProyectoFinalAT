from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from appPasteleria.forms import RegistroUsuarioForm
from appPerfiles.views import obtenerAvatar, datosPerfil


def inicio(request):
    return render(request, 'appPasteleria/index.html')

def register(request):
    if request.method=='POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('first_name')
            form.save()
            return render(request, 'appPasteleria/index.html', {'mensaje':f'Usuario {username} creado correctamente'})
        else:
            return render(request, 'appPasteleria/register.html', {'form':form, 'mensaje':'Error al crear usuario'})

    else:
        form=RegistroUsuarioForm()
    return render(request, 'appPasteleria/register.html', {'form':form})


def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario=authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'appPerfiles/perfil.html', {'imagen':obtenerAvatar(request), 'info':datosPerfil(request)})
            else:
                form=AuthenticationForm()
                return render(request, 'appPasteleria/login.html', {'mensaje':'Usuario o contraseña incorrecto', 'form':form})
        
        else:
            form=AuthenticationForm()
            return render(request, 'appPasteleria/login.html', {'mensaje':'Usuario o contraseña incorrecto', 'form':form})
    else:
        form=AuthenticationForm()
    return render(request, 'appPasteleria/login.html', {'form':form})

def sobreMi(request):
    return render(request, 'appPasteleria/sobreMi.html')


