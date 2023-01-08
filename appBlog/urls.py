from django.urls import path
from appBlog.views import *

urlpatterns = [
    path('agregarArticulo/', crear_articulo, name='agregarArticulo'),
    path('recetas/', ver_recetas, name='ver_receta'),
    path('leerReceta/<id>', leer_receta, name='leer_receta'),
    
]

