from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class informacionPerfil(models.Model):
    fecha_nacimiento=models.DateField()
    ubicacion=models.CharField(max_length=100)
    biografia=models.TextField(default='Hola')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

