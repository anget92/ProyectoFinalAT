from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username=forms.CharField(label= '', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1=forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2=forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'}))

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_text={k:"" for k in fields}