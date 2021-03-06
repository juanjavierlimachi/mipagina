from django.db import models
# Create your models here.
class Proveedor(models.Model):
	Nombre_Razon_Social=models.CharField(max_length=200, unique=True)
	Nit=models.PositiveIntegerField(max_length=15, unique=True)
	Telefono=models.PositiveIntegerField(max_length=8, unique=True)
	Direccion=models.CharField(max_length=150)
	Email=models.EmailField(unique=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return "%s Nit:%s Telf:%s"%(self.Nombre_Razon_Social,self.Nit,self.Telefono)
