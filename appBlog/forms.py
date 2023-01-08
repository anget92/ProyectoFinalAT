from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class agregarArticulo(forms.Form):
    titulo=forms.CharField(max_length=100)
    cuerpo=forms.CharField(widget=CKEditorWidget())
    imagen=forms.ImageField()
    
    
