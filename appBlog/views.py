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

@login_required
def leer_receta(request, id):
    receta=articulo.objects.get(id=id)
    return render(request, 'appBlog/leer_receta.html', {'receta':receta})

@login_required
def mis_recetas(request):
    receta=articulo.objects.filter(autor=request.user)
    return render(request, 'appBlog/misRecetas.html', {'recetas':receta})

@login_required
def eliminar_Receta(request, id):
    receta=articulo.objects.get(id=id)
    receta.delete()
    receta=articulo.objects.filter(autor=request.user)
    return render(request, 'appBlog/misRecetas.html', {'recetas':receta})

@login_required
def editarReceta(request, id):
    receta=articulo.objects.get(id=id)
    if request.method=='POST':
        
        form=agregarArticulo(request.POST, request.FILES)
        

        if form.is_valid():

            diccionario=form.cleaned_data
            
            receta.titulo=diccionario['titulo']
            receta.cuerpo=diccionario['cuerpo']
            receta.imagen=request.FILES['imagen']
            receta.save()
            recetas=articulo.objects.filter(autor=request.user)

            return render(request, 'appBlog/misRecetas.html', {'recetas':recetas})

        else:
            formulario=agregarArticulo(initial={'titulo':receta.titulo, 'cuerpo':receta.cuerpo, 'imagen':receta.imagen})
            return render(request, 'appBlog/editarRecetas.html', {'form':formulario, 'recetas':receta, 'mensaje':'Introdujiste un dato erróneo'})
            


    else:
        formulario=agregarArticulo(initial={'titulo':receta.titulo, 'cuerpo':receta.cuerpo, 'imagen':receta.imagen})

    return render(request, 'appBlog/editarRecetas.html', {'receta':receta,'form':formulario, 'recetas':receta})

