from django.db import models
from mipagina.apps.proveedor.models import *
from mipagina.apps.cliente.models import *
from django.contrib.auth.forms import User
# Create your models here
class Categoria(models.Model):
	Nombre_categoria=models.CharField(max_length=50, unique=True)
	Material=models.CharField(max_length=50)
	fecha_registro = models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.Nombre_categoria
class Producto(models.Model):
	Nombre_producto=models.CharField(max_length=150, unique=True)
	Marca=models.CharField(max_length=50)
	Precio_producto=models.FloatField()
	Stock=models.IntegerField(default=0)
	Usuario=models.ForeignKey(User)
	Categoria=models.ForeignKey(Categoria)
	fecha_registro = models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	archivo=models.FileField(upload_to = 'productos',blank=True, null=True)
	def __unicode__(self):
		return "%s Marca:%s"%(self.Nombre_producto,self.Marca)

class CompraProducto(models.Model):
	Precio_unidad=models.FloatField()
	cantidad=models.PositiveIntegerField()
	producto=models.ForeignKey(Producto)
	proveedor=models.ForeignKey(Proveedor)
	total=models.FloatField()
	fecha_registro=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		#return self.cantidad
		return "%s, %s"%(self.proveedor,self.producto)
class SalidasPro(models.Model):
	Precio_unidad=models.FloatField()
	cantidad=models.PositiveIntegerField()
	producto=models.ForeignKey(Producto)
	total=models.FloatField()
	trabajador=models.ForeignKey(Trabajador)
	fecha_registro=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return "%s, %s"%(self.trabajador,self.producto)
class Reserva(models.Model):
	id_trabajador = models.ForeignKey(Trabajador)
	producto=models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()
	adelanto = models.PositiveIntegerField(default=0)
	Total = models.PositiveIntegerField()
	fecha = models.DateField()
	fecha_registro = models.DateTimeField(auto_now=True)
	estado = models.BooleanField(default=True)
	def __unicode__(self):
		return self.id_trabajador
