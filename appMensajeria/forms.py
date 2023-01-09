from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib.admin.widgets import FilteredSelectMultiple





class formMensaje(forms.Form):
    cuerpo=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Escribe tu mensaje'}) )
    receptor=forms.ModelChoiceField(queryset=User.objects.all())

class formReceptor(forms.Form):
    receptor=forms.CharField()
    
   
