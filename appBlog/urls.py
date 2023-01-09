from django.urls import path
from appBlog.views import *

urlpatterns = [
    path('agregarArticulo/', crear_articulo, name='agregarArticulo'),
    path('recetas/', ver_recetas, name='ver_recetas'),
    path('leerReceta/<id>', leer_receta, name='leer_receta'),
    path('misRecetas/', mis_recetas, name='misRecetas'),
    path('eliminarReceta/<id>', eliminar_Receta, name='eliminarReceta'),
    path('editarReceta/<id>', editarReceta, name='editarReceta'),
    
]

