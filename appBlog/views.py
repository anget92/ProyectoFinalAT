from django.shortcuts import render
from .models import articulo
from .forms import agregarArticulo
from django.contrib.auth.decorators import login_required
from appPerfiles.views import datosPerfil, obtenerAvatar

@login_required
def crear_articulo(request):
    if request.method=='POST':
        form=agregarArticulo(request.POST, request.FILES)
        if form.is_valid():
            diccionario=form.cleaned_data
            titulo=diccionario['titulo']
            cuerpo=diccionario['cuerpo']
            
            imagen=request.FILES['imagen']
            user=request.user

            blog=articulo(titulo=titulo, cuerpo=cuerpo, imagen=imagen, autor=user)

            blog.save()
            return render(request, 'appPerfiles/perfil.html', {'info':datosPerfil(request), 'imagen':obtenerAvatar(request)})
        else:
            return render(request, 'appBlog/agregarArticulo.html', {'form':form})
    else:
        form=agregarArticulo()
    return render(request, 'appBlog/agregarArticulo.html', {'form':form})


def ver_recetas(request):
    recetas=articulo.objects.all().order_by('fecha')
    
    return render(request, 'appBlog/recetas.html', {'recetas':recetas})

def leer_receta(request, id):
    receta=articulo.objects.get(id=id)
    return render(request, 'appBlog/leer_receta.html', {'receta':receta})

