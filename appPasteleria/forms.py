from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username=forms.CharField(label='Nombre de usuario')
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    email=forms.EmailField()
    password1=forms.CharField(label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_text={k:"" for k in fields}