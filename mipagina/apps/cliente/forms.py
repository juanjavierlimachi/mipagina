#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *

class FormTrabajador(ModelForm):
	Nombre_trabajador = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={ 'title': 'Ingrese su Nombe','placeholder':'Ingrese su Nombre','required':'True'}))
	Apellidos = forms.CharField(label="Apellido(s)",widget=forms.TextInput(attrs={'title':'Ingrese su Apellido','placeholder':'Ingrese su Apellido(s)','required':'True'}))
	Ci_Nit = forms.IntegerField(label="Num de CI",widget=forms.PasswordInput(attrs={ 'title': 'Ingrese si Numero de CI','placeholder':'Tu CI sera tu contraseña','required':'True'}))
	Telefono = forms.IntegerField(label="Celular",widget=forms.NumberInput(attrs={ 'title': 'Ingrese su Numero de Celular','placeholder':'Tu Numero de Celular','required':'True'}))
	Email=forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={ 'title': 'Ingrese tu e-mail','placeholder':'Ingrese su e-mail','required':'True'}))
	Direccion = forms.CharField(label="Dirección",widget=forms.TextInput(attrs={ 'title': 'Ingrese su dirección','placeholder':'Ingrese su dirección','required':'True'}))
	#forms.TextInput()
	class Meta():
		model = Trabajador
		exclude=('estado',)
class TrabajadorLoguin(forms.Form):
	tel = forms.IntegerField(required=True,label="Numero de Celular")
	ci = forms.IntegerField(required=True,label="Numero de CI:",widget=forms.PasswordInput(render_value=False))