#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
from .models import *
from .forms import *
from mipagina.apps.producto.models import *
from datetime import datetime, date, time, timedelta
import calendar
# Create your views here.
def NewProveedor(request):
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormProveedor()
	return render_to_response('proveedor/NewProveedor.html',{'forms':forms},context_instance=RequestContext(request))

def VerPrveedor(request):
	datos=Proveedor.objects.all().order_by('-id')
	return render_to_response('proveedor/VerPrveedor.html',{'datos':datos},context_instance=RequestContext(request))

def deleteProveedor(request, id):
	dato=Proveedor.objects.get(id=int(id))
	return render_to_response('proveedor/deleteProveedor.html',{'dato':dato},context_instance=RequestContext(request))
def delProveedor(request, id):
	Proveedor.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se dió de Baja Al registro Correctamente.")

def editProveedor(request, id):
	cod=int(id)
	dato=Proveedor.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormProveedor(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El proveedor se Actualizó Correctamente.")
	else:
		forms=FormProveedor(instance=dato)
	return render_to_response('proveedor/editProveedor.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))

def buscarPro(request):
	if request.method=='POST':
		pass
	else:
		texto=request.GET["q"]
		busqueda=(
				Q(Nombre_Razon_Social__icontains=texto) |
				Q(Nit__icontains=texto) |
				Q(Telefono__icontains=texto)
			)
		resultados=Proveedor.objects.filter(busqueda).distinct()
	return render_to_response('proveedor/buscarPro.html',{'resultados':resultados},context_instance=RequestContext(request))

def buscarProveedor_view(request):
	if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
		texto=request.POST["p"]
		busqueda=(
			Q(Nombre_Razon_Social__icontains=texto) |
			Q(Nit__icontains=texto) |
			Q(Telefono__icontains=texto)
		)
		resultados=Proveedor.objects.filter(busqueda).distinct()
		print "Clente:",resultados
		return render_to_response('proveedor/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET["p"]
		busqueda=(
			Q(Nombre_Razon_Social__icontains=texto) |
			Q(Nit__icontains=texto) |
			Q(Telefono__icontains=texto)
		)
		resultados=Proveedor.objects.filter(busqueda).distinct()
        # html="<ul class='ul_lista'>"
        # for i in resultados:
        #     html=html+"<li><a href='/detalles/"+str(i.id)+"/'>"+i.Nombre_trabajador+""+i.Apellidos+"</a></li>"
        # html=html+"<ul>"
		return render_to_response('proveedor/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))
def empresa(request,id):
	persona=Proveedor.objects.get(id=int(id))
	fecha=datetime.now()
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
    #la linea de abajo Consultamos todas las selidas q el cliente realizo con el MES 
	ventas=CompraProducto.objects.filter(proveedor=int(id), fecha_registro__gte=dateMonthStart, estado=0).order_by("-id")
	pagado=CompraProducto.objects.filter(proveedor=int(id), fecha_registro__gte=dateMonthStart, estado=0)
	totaoPagado=0
	cont=0
	for p in pagado:
		totaoPagado += p.total
		cont = cont + 1
    #cont=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart, estado=0).count()
	dic={
		'ventas':ventas,
		'cont':cont,
		'persona':persona,
		'totaoPagado':totaoPagado
	}
	return render_to_response('proveedor/empresa.html',dic,context_instance=RequestContext(request))