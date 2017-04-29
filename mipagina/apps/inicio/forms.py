#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Perfiles
from django.contrib.auth.forms import User
class UserForm(UserCreationForm):
	username = forms.CharField(max_length=40,required=True,label="Nombre de Usuario")
	password1 = forms.CharField(required=True,label="Contraseña",widget=forms.PasswordInput(render_value=False))
	password2 = forms.CharField(required=True, label="Confirmación",widget=forms.PasswordInput(render_value=False))
	first_name = forms.CharField(max_length=40,required=True, label="Nombre Completo")
	last_name = forms.CharField(max_length=50,required=True, label="Apellido(s)")
	email = forms.EmailField(required=True,label='Correo Electrónico')
	ci = forms.IntegerField(required=True,label="Nro. de CI.")
	telefono = forms.IntegerField(required=True,label="Telefono/Celular")
	def clean_ci(self):
		ci=self.cleaned_data['ci']
		if len(str(ci))>7 or len(str(ci))<=5:
			raise forms.ValidationError('El Nro. de CI. deve ser 6 dígitos')
		try:
			p=Perfiles.objects.get(ci=ci)
		except Perfiles.DoesNotExist:
			return ci
		raise forms.ValidationError('El Nro. de CI. ya Existe')
	def clean_telefono(self):
		telefono=self.cleaned_data['telefono']
		if len(str(telefono))>9 or len(str(telefono))<=7:
			raise forms.ValidationError('El Nro. de Teléfono deve ser 8 dígitos')
		try:
			p = Perfiles.objects.get(telefono=telefono)
		except Perfiles.DoesNotExist:
			return telefono
		raise forms.ValidationError('El Numero de Teléfono ya Existe')
	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			p = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('El E-mail no deve ser Repetido')
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
		widgets = {
			'password1':forms.PasswordInput(),
		}
	def save(self,commit=True):
		user=super(UserForm,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get('email')
		if commit:
			user.save()
		return user
#formularios para editar el usuario
class formPerfiles(forms.ModelForm):
	class Meta:
		model=Perfiles
		exclude=['usuario']
class UserForms(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','first_name','last_name','email')
		#exclude=['password']

class CambioForm(forms.Form):
	Nueva_Contracenia= forms.CharField(required=True, label="Contraseña",widget=forms.PasswordInput(render_value=False))
	Confirmacion	 = forms.CharField(required=True, label="Confirmar",widget=forms.PasswordInput(render_value=False))
	def password(self):
		pass_one=self.cleaned_data['Nueva_Contracenia']
		pass_tho=self.cleaned_data['Confirmacion']
		if pass_one == pass_tho:
			pass
		else:
			raise forms.ValidationError('Los datos no Coinsiden')

class CrearBaku(forms.Form):
	Usuario=forms.CharField(required=True,max_length=40)
	Password=forms.CharField(required=True, label="Contraseña",widget=forms.PasswordInput(render_value=False))

class formDB(forms.Form):
	base=forms.FileField()
