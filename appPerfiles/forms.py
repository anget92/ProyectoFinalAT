from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='Imagen')

class agregarInfoPerfil(forms.Form):
    fecha_nacimiento=forms.DateTimeField(widget=forms.SelectDateWidget(years=range(1900,2010)))
    ubicacion=forms.CharField(max_length=100)
    biografia=forms.CharField(widget=CKEditorWidget())