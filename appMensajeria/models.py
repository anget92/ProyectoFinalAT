from django.db import models
from django.contrib.auth.models import User

class mensaje(models.Model):
    emisor=models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receptor=models.ForeignKey(User, related_name='reciever', on_delete=models.CASCADE)
    cuerpo=models.CharField(max_length=200)
    fecha=models.DateTimeField(auto_now_add=True)
    leido=models.BooleanField(default=False)
