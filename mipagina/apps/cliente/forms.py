#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *

class FormTrabajador(ModelForm):
	Nombre_trabajador = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={ 'title': 'Ingrese su Nombe','placeholder':'Ingrese su Nombre','required':'True'}))
	Apellidos = forms.CharField(label="Apellido(s)",widget=forms.TextInput(attrs={'title':'Ingrese su Apellido','placeholder':'Ingrese su Apellido','required':'True'}))
	Ci_Nit = forms.IntegerField(widget=forms.PasswordInput(attrs={ 'title': 'Ingrese si Numero de CI','placeholder':'Tu CI sera tu contraseña','required':'True'}))
	Telefono = forms.IntegerField(widget=forms.NumberInput(attrs={ 'title': 'Ingrese su Numero de Celular','placeholder':'Tu Numero de Celular','required':'True'}))
	Email=forms.EmailField(widget=forms.EmailInput(attrs={ 'title': 'Ingrese tu e-mail','placeholder':'Ingresse tu e-mail','required':'True'}))
	Direccion = forms.CharField(widget=forms.TextInput(attrs={ 'title': 'Ingrese su dirección','placeholder':'Ingrese su dirección','required':'True'}))
	#forms.TextInput()
	class Meta():
		model = Trabajador
		exclude=('estado',)
class TrabajadorLoguin(forms.Form):
	tel = forms.IntegerField(required=True,label="Numero de Celular")
	ci = forms.IntegerField(required=True,label="Numero de CI:",widget=forms.PasswordInput(render_value=False))