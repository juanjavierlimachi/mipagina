#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *

class FormProveedor(ModelForm):
	Telefono = forms.IntegerField(required=True,label='Teléfono')
	Direccion = forms.CharField(required=True,max_length=150 ,label='Dirección')
	class Meta():
		model = Proveedor
		exclude=('estado',)