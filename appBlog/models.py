from django.db import models
from django.contrib.auth.models import User

class articulo(models.Model):
    titulo=models.CharField(max_length=100)
    cuerpo=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='img_blogs/')
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def snippet(self):
        return self.cuerpo[:200] + '...'
    