#encoding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from .forms import *
from mipagina.apps.proveedor.models import *
from mipagina.apps.proveedor.forms import *
from django.db.models import Q
from mipagina.apps.cliente.models import *
import json

from datetime import datetime, date, time, timedelta
import calendar

import calendar
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string

# Create your views here.
def newCategoria(request):
	if request.method=='POST':
		form=FormCategoria(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("ok")
	else:
		form=FormCategoria()
	return render_to_response('producto/newCategoria.html',{'form':form},context_instance=RequestContext(request))

def verCategoria(request):
	datos=Categoria.objects.all().order_by("-id")
	cont=Categoria.objects.filter(estado=0).count()
	return render_to_response('producto/verCategoria.html',{'datos':datos,'cont':cont}, context_instance=RequestContext(request))
def NewProducto(request):
	if request.method =='POST':
		Usuario=Producto(Usuario=request.user)
		forms=FormProducto(request.POST,request.FILES,instance=Usuario, )
		if forms.is_valid():
			try:
				existe = Producto.objects.get(Nombre_producto=request.POST['Nombre_producto'])
				return HttpResponse("El Producto ya existe.")
			except Producto.DoesNotExist:
				forms.save()
				return HttpResponse("ok")
		else:
			return HttpResponse("El Producto ya existe.")
	else:
		forms=FormProducto()
	return render_to_response('producto/NewProducto.html',{'forms':forms}, context_instance=RequestContext(request))

def VerProductos(request):
	datos=Producto.objects.all().order_by("-id")
	baja=Producto.objects.filter(estado=1).count()#en Baja
	cont=Producto.objects.filter(estado=0).count()#Alta
	total=Producto.objects.all().count()#Todos los proudctos
	forms=FormCompra()
	categorias=Categoria.objects.filter(estado=0).order_by('-id')
	dic={'datos':datos, 'cont':cont,'forms':forms,'categorias':categorias,'total':total,'baja':baja}
	#print request.session.session_key

	return render_to_response('producto/VerProductos.html',dic, context_instance=RequestContext(request))
def addProducto(request, id):
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Registro Exitoso")
	else:
		forms=FormProveedor()
	return render_to_response('proveedor/NewProveedor.html',{'forms':forms},context_instance=RequestContext(request))

def deleteCate(request, id):
	dato=Categoria.objects.get(id=int(id))
	return render_to_response('producto/deleteCate.html',{'dato':dato},context_instance=RequestContext(request))
def delCate(request, id):
	Categoria.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se dió de Baja Al registro Correctamente.")

def editCate(request, id):
	cod=int(id)
	dato=Categoria.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormCategoria(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La Categoria se Actualizó Correctamente.")
	else:
		forms=FormCategoria(instance=dato)
	return render_to_response('producto/editCate.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))

def deleteProducto(request, id):
	dato=Producto.objects.get(id=int(id))
	return render_to_response('producto/deleteProducto.html',{'dato':dato},context_instance=RequestContext(request))
def delProducto(request, id):
	Producto.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se dió de Baja Al registro Correctamente.")
def editProducto(request, id):
	cod=int(id)
	dato=Producto.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormProducto(request.POST,request.FILES ,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El Producto se Actualizó Correctamente.")
	else:
		forms=FormProducto(instance=dato)
	return render_to_response('producto/editProducto.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def addCompra(request, id):
	cod=int(id)
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El Producto se Actualizó Correctamente.")
	else:
		forms=FormProveedor()
	return render_to_response('producto/addCompra.html',{'cod':cod,'forms':forms},context_instance=RequestContext(request))


def IngresaProducto(request):
	if request.method=='POST':
		forms=FormCompra(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Se Registró los datos Carrectamente.")
	else:
		forms=FormCompra()
	return render_to_response('producto/IngresaProducto.html',{'forms':forms},context_instance=RequestContext(request))

def Ingresos(request, id):
	producto=id
	compras=CompraProducto()
	exito=False
	compras.Precio_unidad=request.GET['pre']
	compras.cantidad=request.GET['conta']
	compras.producto_id=producto
	compras.proveedor_id=request.GET['prov']
	compras.save()
	exito=True
	print "Compra realizada"
	if exito==True:
		dato=CompraProducto.objects.all().order_by('-id')[0:1]
		actual=Producto.objects.get(id=int(id))
		actual=actual.Stock+int(request.GET['conta'])
		print "Actual",actual
		Producto.objects.filter(id=int(id)).update(Stock=actual)
		print dato
	return render_to_response('producto/Ingresos.html',{'exito':exito,'dato':dato},context_instance=RequestContext(request))
def por_categorias(request, id):
	datos=Producto.objects.filter(Categoria=int(id)).order_by('-id')
	cont=Producto.objects.filter(Categoria=int(id)).count()
	forms=FormCompra()
	cate=Categoria.objects.get(id=int(id))
	return render_to_response('producto/por_categorias.html',{'datos':datos,'forms':forms,'cont':cont,'cate':cate},context_instance=RequestContext(request))
def stock_de_productos(request, id):
	valor = int(id)
	print "Volar",valor
	if valor == 0 :
		datos=Producto.objects.filter(Stock=int(id)).order_by('-id')
		cont=Producto.objects.filter(Stock=int(id), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 1:
		datos=Producto.objects.filter(Stock__range=(1,9)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(1,9), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 2:
		datos=Producto.objects.filter(Stock__range=(10,24)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(10,24), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 3:
		datos=Producto.objects.filter(Stock__range=(25,59)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(25,59), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 4:
		datos=Producto.objects.filter(Stock__gte=60).order_by('-id')
		cont=Producto.objects.filter(Stock__gte=60, estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))

def salidas(request, id):
	id_pro=int(id)
	maximo = 0
	t = ''
	if len(request.session['carrito']) > 0:
		maximo = max(request.session['carrito'])#optengo el mayor elemento de la lista
		print "Valor maxilo",maximo
		query = SalidasPro.objects.get(id=int(maximo))
		dato = query.trabajador_id
		t = Trabajador.objects.get(id=int(dato))
		print t.Nombre_trabajador
	return render_to_response('producto/salidas.html',{'id_pro':id_pro,'maximo':maximo,'t':t},context_instance=RequestContext(request))


from django.core import serializers
def BuscarTrab(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		id_producto=request.GET['producto']
		print "ESTE ES EL PRODUCTOOOOO",id_producto
		datoProducto=Producto.objects.get(id=int(id_producto))
		busqueda=(
			Q(Nombre_trabajador__icontains=trabajador) |
			Q(Apellidos__icontains=trabajador) |
			Q(Ci_Nit__icontains=trabajador)
		)
		resultados=Trabajador.objects.filter(busqueda).distinct()
		#data = serializers.serialize('json', resultados) dos linas para traer datos en formato JSON
		#return HttpResponse(data,content_type="application/json")
		#return HttpResponse(json.dumps({"data":data}),content_type="application/json")
		request.session['carrito']=[]

		return render_to_response('cliente/buscarTrabjador.html',{'resultados':resultados,'datoProducto':datoProducto},context_instance=RequestContext(request))
	else:
		return HttpResponse("No se encontraron coinsidencias")
def SalidaProducto(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		trab=Trabajador.objects.get(id=int(request.GET['trabajador']))
		print 'Estes el el trabajador',trabajador
		print request.GET['producto']
		producto=Producto.objects.get(id=int(request.GET['producto']))
		#forms=FormSalidas()
		#return HttpResponse("Error.")
		return render_to_response('producto/SalidaProducto.html',{'trabajador':trabajador,'producto':producto,'trab':trab},context_instance=RequestContext(request))

def SalidaProductoCliente(request):
	estado=False
	pre = Producto.objects.get(id=int(request.POST['prod']))
	salida=SalidasPro()
	salida.Precio_unidad=float(pre.Precio_producto)
	salida.cantidad=int(request.POST['cant'])
	salida.total=float(pre.Precio_producto)*float(request.POST['cant'])
	salida.producto_id=int(request.POST['prod'])
	salida.trabajador_id=int(request.POST['trab'])
	total=float(pre.Precio_producto)*float(request.POST['cant'])
	estado=True
	siestado = Producto.objects.get(id=int(request.POST['prod']))#Berifico es el producto esta con baja
	if estado == True and siestado.estado == 0:
		dato = Producto.objects.get(id=int(request.POST['prod']))
		if dato.Stock >= int(request.POST['cant']) and dato.Stock>0:
			if siestado.Precio_producto == float(pre.Precio_producto):
				salida.save()
				actual=dato.Stock-int(request.POST['cant'])
				Producto.objects.filter(id=int(request.POST['prod'])).update(Stock=actual)
				ultimoSalida=salida.id
				lista=request.session['carrito']
				lista.append(int(ultimoSalida))
				print lista
				request.session['carrito']=lista
				print "salida",ultimoSalida
				salidas=SalidasPro.objects.get(id=int(ultimoSalida))
				#return render_to_response('producto/SalidaProductoCliente.html',{'salidas':salidas,'total':total},context_instance=RequestContext(request))
				return HttpResponse("ok")
			else:
				return HttpResponse("Error el Precio del Producto deve ser Igual a lo Registrado.")
		else:
			return HttpResponse("No hay suficientes productos para realizar la salida.")
	else:
		return HttpResponse("Error en los datos. El producto No puede estar en Baja")
def get_retorna_salidas(request):
	productos=request.session['carrito']
	salidas=SalidasPro.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				#return render_to_response("producto/get_retorna_salidas.html",{'aux':aux},context_instance=RequestContext(request))
				traba=j.trabajador
				Numcontrol+=str(j.id)+':'
	total_pago=0
	contidadPro=len(out)
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	dic={
		'pagesize':'A4',
		'Numcontrol':Numcontrol,
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'out':out,
		'total_pago':total_pago,
		'traba':traba,
		'contidadPro':contidadPro
	}
	html=render_to_string("producto/get_retorna_salidas.html",dic,context_instance=RequestContext(request))
	return generar_pdf(html)
def get_retorna_salidas_view(request):
	productos=request.session['carrito']
	salidas=SalidasPro.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				#return render_to_response("producto/get_retorna_salidas.html",{'aux':aux},context_instance=RequestContext(request))
				traba=j.trabajador
				Numcontrol+=str(j.id)+':'
	total_pago=0
	contidadPro=len(out)
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	dic={
		'pagesize':'A4',
		'Numcontrol':Numcontrol,
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'out':out,
		'total_pago':total_pago,
		'traba':traba,
		'contidadPro':contidadPro
	}
	return render_to_response("producto/get_retorna_salidas.html",dic,context_instance=RequestContext(request))
def CantidadSalida(request):
	productos=request.session['carrito']
	contidadPro=len(productos)
	return HttpResponse(contidadPro)
def CantidadIngresos(request):
	productos=request.session['ingreso']
	contidadPro=len(productos)
	return HttpResponse(contidadPro)


def IngresosP(request, id):
	id_pro=int(id)
	maximo = 0
	t = ''
	if len(request.session['ingreso']) > 0:
		maximo = max(request.session['ingreso'])#optengo el mayor elemento de la lista
		print "Valor maxilo",maximo
		query = CompraProducto.objects.get(id=int(maximo))
		dato = query.proveedor_id
		t = Proveedor.objects.get(id=int(dato))
		print t.Nombre_Razon_Social
	return render_to_response('producto/IngresosP.html',{'id_pro':id_pro,'maximo':maximo,'t':t},context_instance=RequestContext(request)) 

def BuscarProveedor(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		id_producto=request.GET['producto']
		print "ESTE ES EL PRODUCTOOOOO",id_producto
		datoProducto=Producto.objects.get(id=int(id_producto))
		busqueda=(
			Q(Nombre_Razon_Social__icontains=trabajador) |
			Q(Nit__icontains=trabajador) |
			Q(Telefono__icontains=trabajador)
		)
		resultados=Proveedor.objects.filter(busqueda).distinct()
		#data = serializers.serialize('json', resultados) dos linas para traer datos en formato JSON
		#return HttpResponse(data,content_type="application/json")
		#return HttpResponse(json.dumps({"data":data}),content_type="application/json")
		request.session['ingreso']=[]
		return render_to_response('proveedor/BuscarProveedor.html',{'resultados':resultados,'datoProducto':datoProducto},context_instance=RequestContext(request))
	else:
		return HttpResponse("No se encontraron coinsidencias")

def IngresosProductos(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		trab=Proveedor.objects.get(id=int(request.GET['trabajador']))
		print 'Estes el el trabajador',trabajador
		producto=Producto.objects.get(id=int(request.GET['producto']))
		print 'ID producto',producto
		return render_to_response('producto/IngresosProductos.html',{'trabajador':trabajador,'producto':producto,'trab':trab},context_instance=RequestContext(request))

def IngresoProductoCliente(request):
	estado=False
	pre = Producto.objects.get(id=int(request.POST['prod']))
	salida=CompraProducto()
	salida.Precio_unidad=float(pre.Precio_producto)
	salida.cantidad=int(request.POST['cant'])
	salida.producto_id=int(request.POST['prod'])
	salida.proveedor_id=int(request.POST['trab'])
	salida.total=float(pre.Precio_producto)*float(request.POST['cant'])
	total=float(pre.Precio_producto)*float(request.POST['cant'])
	print "Total a Pagar",total
	estado=True
	siestado = Producto.objects.get(id=int(request.POST['prod']))#Berifico que el producto no este con baja
	if estado == True and siestado.estado == 0:
		dato = Producto.objects.get(id=int(request.POST['prod']))
		if int(request.POST['cant']) > 0:
			if siestado.Precio_producto == float(pre.Precio_producto):
				salida.save()
				actual=dato.Stock+int(request.POST['cant'])
				Producto.objects.filter(id=int(request.POST['prod'])).update(Stock=actual)
				ultimoSalida=salida.id
				print "Ingresooo",ultimoSalida
				lista=request.session['ingreso']
				lista.append(int(ultimoSalida))
				request.session['ingreso']=lista
				salidas=CompraProducto.objects.get(id=int(ultimoSalida))
				#return render_to_response('producto/SalidaProductoCliente.html',{'salidas':salidas,'total':total},context_instance=RequestContext(request))
				return HttpResponse('ok')
			else:
				return HttpResponse("Error el Precio de Producto no Coinside con lo registrado.")
		else:
			return HttpResponse("Error no se puede Ingresar un valor Negativo.")
	else:
		return HttpResponse("Error en los datos. El producto No puede estar en Baja")

def get_retorna_ingresos(request):
	productos=request.session['ingreso']
	salidas=CompraProducto.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				traba=j.proveedor
				Numcontrol+=str(j.id)+':'
	total_pago=0
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	user=request.user
	html=render_to_string("producto/get_retorna_ingresos.html",{'Numcontrol':Numcontrol,'user':user,'fecha':fecha,'productos':productos,'salidas':salidas,'out':out,'total_pago':total_pago,'traba':traba},context_instance=RequestContext(request))
	return generar_pdf(html)
def get_retorna_ingresos_view(request):
	productos=request.session['ingreso']
	salidas=CompraProducto.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				traba=j.proveedor
				Numcontrol+=str(j.id)+':'
	total_pago=0
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	user=request.user
	return render_to_response("producto/get_retorna_ingresos.html",{'Numcontrol':Numcontrol,'user':user,'fecha':fecha,'productos':productos,'salidas':salidas,'out':out,'total_pago':total_pago,'traba':traba},context_instance=RequestContext(request))

def uploadFiles(request):
	return render_to_response('producto/uploadFiles.html',{},context_instance=RequestContext(request))

def kardex(request, id):
	producto=Producto.objects.get(id=int(id))
	valor = float(producto.Precio_producto) * float(producto.Stock)
	fecha=datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(id)).order_by("-id")[0:1]
	Bsalidas=SalidasPro.objects.filter(producto=int(id))
	bs = 0
	for sa in Bsalidas:
		bs  = float(sa.Precio_unidad) + float(bs)
	Bingresos=CompraProducto.objects.filter(producto=int(id))
	bsi = 0
	for i in Bingresos:
		bsi  = float(i.Precio_unidad) + float(bsi)
	dic={
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul,
		'bs':bs,
		'bsi':bsi,
		'valor':valor
	}
	return render_to_response('producto/kardex.html',dic,context_instance=RequestContext(request))

def inProduct(request):
	if request.method=='POST':
		inicio=datetime.strptime(request.POST['inicio'],"%d/%m/%Y")
		final=datetime.strptime(request.POST['final'],"%d/%m/%Y")
		if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
		final = final + timedelta(days=1)
		user=int(request.POST['user'])
		t_ingresos=CompraProducto.objects.filter(proveedor_id=user,fecha_registro__range=(inicio,final)).count()
		datos=CompraProducto.objects.filter(proveedor_id=user,fecha_registro__range=(inicio,final))
		proveedor = Proveedor.objects.get(id=user)
		total = 0
		for i in datos:
			total = total + i.total
		dat={
			'ingresos':datos,
			't_ingresos':t_ingresos,
			'proveedor':proveedor,
			'total':total
		}
		return render_to_response('producto/rangoIngresos.html',dat,context_instance=RequestContext(request))
	fecha=datetime.now()#Caonsalta desde el 1 dia del mes
	#fecha=fecha.strftime('%Y-%m-%d')
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
	dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month+1)[1])
	print "Incioooo", dateMonthStart
	print "Fecha final", dateMonthEnd
	usuarios=Proveedor.objects.all().order_by("-id")
	ingresos=CompraProducto.objects.filter(fecha_registro__range=(dateMonthStart,fecha)).order_by('-id')
	t_ingresos=CompraProducto.objects.filter(fecha_registro__range=(dateMonthStart,fecha),estado=0).count()
	dic={
		'ingresos':ingresos,
		't_ingresos':t_ingresos,
		'usuarios':usuarios
	}
	return render_to_response('producto/inProduct.html',dic,context_instance=RequestContext(request))
def outProduct(request):
	if request.method=='POST':
		inicio=datetime.strptime(request.POST['inicio'],"%d/%m/%Y")
		final=datetime.strptime(request.POST['final'],"%d/%m/%Y")
		if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
		final = final + timedelta(days=1)
		user=int(request.POST['user'])
		t_ingresos=SalidasPro.objects.filter(trabajador_id=user,fecha_registro__range=(inicio,final)).count()
		datos=SalidasPro.objects.filter(trabajador_id=user,fecha_registro__range=(inicio,final))
		proveedor = Trabajador.objects.get(id=user)
		total = 0
		for i in datos:
			total = total + i.total
		dat={
			'ingresos':datos,
			't_ingresos':t_ingresos,
			'proveedor':proveedor,
			'total':total
		}
		return render_to_response('producto/rangoSalidas.html',dat,context_instance=RequestContext(request))
	fecha=datetime.now()
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
	dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month+1)[1])
	salidas=SalidasPro.objects.filter(fecha_registro__range=(dateMonthStart,fecha)).order_by('-id')
	t_salidas=SalidasPro.objects.filter(fecha_registro__range=(dateMonthStart,fecha),estado=0).count()
	usuarios=Trabajador.objects.all().order_by("-id")
	dic={
		'salidas':salidas,
		't_salidas':t_salidas,
		'usuarios':usuarios
	}
	return render_to_response('producto/outProduct.html',dic,context_instance=RequestContext(request))
def ReportesProducto(request):
	fecha=datetime.now()
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
	dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month+1)[1])
	productos=Producto.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha)).order_by("-id")
	salidas=SalidasPro.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha)).order_by("-id")
	ingresos=CompraProducto.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha)).order_by("-id")
	total=Producto.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha)).count()
	dic={
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'ingresos':ingresos,
		'total':total
	}
	html = render_to_string('producto/ReportesProducto.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)
def deleteSalidas(request, id):
	dato=SalidasPro.objects.get(id=int(id))
	return render_to_response('producto/deleteSalidas.html',{'dato':dato},context_instance=RequestContext(request))

def deleteSalidasConfir(request, id):
	if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
		SalidasPro.objects.filter(id=int(id)).update(estado=1)
		return HttpResponse("Se dió de Baja Al registro Correctamente.")
	else:
		return HttpResponse("Ud. no esta autenticado por favor inicie sesión")

def deleteIngresos(request, id):
	dato=CompraProducto.objects.get(id=int(id))
	return render_to_response('producto/deleteIngresos.html',{'dato':dato},context_instance=RequestContext(request))

def deleteIngresosConfir(request, id):
	if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
		CompraProducto.objects.filter(id=int(id)).update(estado=1)
		return HttpResponse("Se dió de Baja Al registro Correctamente.")
	else:
		return HttpResponse("Ud. no esta autenticado por favor inicie sesión")
def editIngresos(request, id):
	cod=int(id)
	dato=CompraProducto.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormCompra(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			precio=CompraProducto.objects.get(id=int(id))
			pago = float(precio.Precio_unidad) * float(precio.cantidad)
			CompraProducto.objects.filter(id=int(id)).update(total = pago)
			return HttpResponse("Los Datos se actualizaron Correctamente.")
	else:
		forms=FormCompra(instance=dato)
	return render_to_response('producto/editIngresos.html',{'forms':forms,'cod':cod,'dato':dato},context_instance=RequestContext(request))

def editSalidas(request, id):
	cod=int(id)
	dato=SalidasPro.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormSalidas(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			precio = SalidasPro.objects.get(id=int(id))
			pago = float(precio.Precio_unidad) * float(precio.cantidad)
			SalidasPro.objects.filter(id=int(id)).update(total = pago)
			return HttpResponse("Los Datos se actualizaron Correctamente.")
	else:
		forms=FormSalidas(instance=dato)
	return render_to_response('producto/editSalidas.html',{'forms':forms,'cod':cod,'dato':dato},context_instance=RequestContext(request))
def buscarProducto_view(request):
	if request.method=="POST":
		texto = request.POST['p']
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		print "coinsidencias",resultados
		return render_to_response('producto/buscarProducto_view.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET['p']
		print texto
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto_view.html',{'resultados':resultados},context_instance=RequestContext(request))
def ShearProduc(request, id):
	producto=Producto.objects.get(id=int(id))
	return render_to_response('producto/ShearProduc.html',{'producto':producto},context_instance=RequestContext(request))

def deleteProductoRecuperar(request, id):
	if request.user.is_authenticated and request.user.is_superuser and request.user.is_active:
		dato=Producto.objects.get(id=int(id))
		return render_to_response('producto/recuperar.html',{'dato':dato},context_instance=RequestContext(request))
	else:
		HttpResponse("Ud. no esta autorizado para hacer esta operación")
def recupera(request, id):
	Producto.objects.filter(id=int(id)).update(estado=0)
	return HttpResponse("El Producto se dió de Alta Correctamente.")
def capturaImg(request):
	return render(request,'producto/capturaImg.html',context_instance=RequestContext(request))
def captura_qr(request):
	categorias=Categoria.objects.filter(estado=0).order_by("-id")
	return render(request,'producto/captura_qr.html',{'categorias':categorias},context_instance=RequestContext(request))
def detaleProducto(request):
	#id=Producto.objects.all().order_by('-id')[1]
	producto=Producto.objects.latest('id')#optiene el ultimo producto(id) registrado
	fecha=datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(producto.id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(producto.id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(producto.id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(producto.id)).order_by("-id")[0:1]
	dic={
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul
	}
	return render_to_response('producto/kardex.html',dic,context_instance=RequestContext(request))

def ImprimirKardex(request, id):
	producto=Producto.objects.get(id=int(id))
	valor = float(producto.Precio_producto) * float(producto.Stock)
	fecha=datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(id)).order_by("-id")[0:1]
	Bsalidas=SalidasPro.objects.filter(producto=int(id))
	bs = 0
	for sa in Bsalidas:
		bs  = float(sa.Precio_unidad) + float(bs)
	Bingresos=CompraProducto.objects.filter(producto=int(id))
	bsi = 0
	for i in Bingresos:
		bsi  = float(i.Precio_unidad) + float(bsi)
	dic={
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul,
		'bs':bs,
		'bsi':bsi,
		'valor':valor
	}
	html = render_to_string('producto/imprimirkardex.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)

def ImprimiarIngresos(request, id,inicio, fin):
	inicio=inicio
	inicio=datetime.strptime(inicio,"%d-%m-%Y")
	final=fin
	final=datetime.strptime(final,"%d-%m-%Y")
	if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
	final = final + timedelta(days=1)
	user=int(id)
	t_ingresos=CompraProducto.objects.filter(proveedor_id=user,fecha_registro__range=(inicio,final)).count()
	datos=CompraProducto.objects.filter(proveedor_id=user,fecha_registro__range=(inicio,final))
	total = 0
	for i in datos:
		total = total + i.total
	proveedor = Proveedor.objects.get(id=user)
	dat={
		'pagesize':'A4',
		'ingresos':datos,
		't_ingresos':t_ingresos,
		'proveedor':proveedor,
		'total':total
	}
	html=render_to_string('producto/ImrangoIngresos.html',dat,context_instance=RequestContext(request))
	return generar_pdf(html)
def ImprimiarSalidas(request, id, inicio,fin):
	inicio=inicio
	inicio=datetime.strptime(inicio,"%d-%m-%Y")
	final=fin
	final=datetime.strptime(final,"%d-%m-%Y")
	if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
	final = final + timedelta(days=1)
	user=int(id)
	t_ingresos=SalidasPro.objects.filter(trabajador_id=user,fecha_registro__range=(inicio,final)).count()
	datos=SalidasPro.objects.filter(trabajador_id=user,fecha_registro__range=(inicio,final))
	total = 0
	for i in datos:
		total = total + i.total
	proveedor = Trabajador.objects.get(id=user)
	dat={
		'pagesize':'A',
		'ingresos':datos,
		't_ingresos':t_ingresos,
		'proveedor':proveedor,
		'total':total
	}
	html=render_to_string('producto/ImrangoSalidas.html',dat,context_instance=RequestContext(request))
	return generar_pdf(html)


def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),'application/pdf')
	return HttpResponse("Error al generar el reporte")

def update_session(request):
	request.session['carrito']=[]
	request.session['ingreso']=[]
	resp="Ahora Puedes Realizar un Nuevo Movimiento de Producto"
	return HttpResponse(resp)

def oprtenerDatos(request):
	dato=int(request.GET['dato'])
	cont = 0
	try:
		producto = Producto.objects.get(id=dato)
		cont = producto.Stock + 1
		print "este es el valor:",producto
		Producto.objects.filter(id=dato).update(Stock=cont)
		return HttpResponse("Ingreso Correctamente el Producto: %s <img src='/static/img/bien.gif'></img>"%producto)
	except Producto.DoesNotExist:
		return HttpResponse("El producto No Existe Verigique por favor.")


def buscarProducto(request):
	if request.method=="GET":
		texto=request.GET["Nombre_producto"]
		busqueda=(
			Q(Nombre_producto__icontains=texto) |
			Q(Nombre_producto__icontains=texto) |
			Q(Marca__icontains=texto)
		)
		resultados=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto.html',{'resultados':resultados},context_instance=RequestContext(request))

def ImprmirCli(request, datos):
	dato = datos.split(",")
	dato = map(int, dato)
	print "datos::",dato
	salidas = SalidasPro.objects.filter(estado=0).order_by("-id")
	cont = 0
	pago = 0
	trabajador = ''
	for i in dato:
		for j in salidas:
			if i == j.id:
				trabajador = j.trabajador
				cont +=1
				pago += j.total
	dic = {
		'dato':dato,
		'salidas':salidas,
		'cont':cont,
		'trabajador':trabajador,
		'pago':pago
	}
	html = render_to_string('producto/ImprmirCli.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)
def ImprmirPro(request, datos):
	dato = datos.split(",")
	dato = map(int, dato)
	print "datos::",dato
	salidas = CompraProducto.objects.filter(estado=0).order_by("-id")
	cont = 0
	pago = 0
	trabajador = ''
	for i in dato:
		for j in salidas:
			if i == j.id:
				trabajador = j.proveedor
				cont +=1
				pago += j.total
	dic = {
		'dato':dato,
		'salidas':salidas,
		'cont':cont,
		'trabajador':trabajador,
		'pago':pago
	}
	html = render_to_string('producto/ImprmirPro.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)
def estadistico(request):
	salidas = SalidasPro.objects.all().count()
	ingresos = CompraProducto.objects.all().count()
	productosAlta = Producto.objects.filter(estado=0).count()
	productoBaja = Producto.objects.filter(estado=1).count()
	reservas = Reserva.objects.filter(estado=1).count()
	dic={
		'salidas':salidas,
		'ingresos':ingresos,
		'productosAlta':productosAlta,
		'productoBaja':productoBaja,
		'reservas':reservas
	}
	return render(request,'producto/estadistico.html',dic,context_instance=RequestContext(request))

def newReserva(request):
	datos = Producto.objects.all()
	request.session['datos'] = []
	enbaja = Reserva.objects.filter(estado=0).count()
	enalta = Reserva.objects.filter(estado=1).count()
	tregistros = Reserva.objects.count()
	dic={
		'datos':datos,
		'enbaja':enbaja,
		'enalta':enalta,
		'tregistros':tregistros
	}
	return render(request, 'producto/newReserva.html',dic,context_instance=RequestContext(request))

def salidasRe(request, id):
	id_pro=int(id)
	maximo = 0
	t = ''
	if len(request.session['reserva']) > 0:
		maximo = max(request.session['reserva'])#optengo el mayor elemento de la lista
		print "Valor maxilo",maximo
		query = Reserva.objects.get(id=int(maximo))
		dato = query.id_trabajador_id
		t = Trabajador.objects.get(id=int(dato))
		print t.Nombre_trabajador#en este plantilla busco un trabajador
	return render_to_response('producto/salidasRe.html',{'id_pro':id_pro,'maximo':maximo,'t':t},context_instance=RequestContext(request))
def BuscarTrabRe(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		id_producto=request.GET['producto']
		print "ESTE ES EL PRODUCTOiiii",id_producto
		datoProducto=Producto.objects.get(id=int(id_producto))
		busqueda=(
			Q(Nombre_trabajador__icontains=trabajador) |
			Q(Apellidos__icontains=trabajador) |
			Q(Ci_Nit__icontains=trabajador)
		)
		resultados=Trabajador.objects.filter(busqueda).distinct()
		request.session['reserva']=[]
		return render_to_response('cliente/buscarTrabjadorRE.html',{'resultados':resultados,'datoProducto':datoProducto},context_instance=RequestContext(request))
	else:
		return HttpResponse("No se encontraron coinsidencias")

def GuardarReserva(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		trab=Trabajador.objects.get(id=int(request.GET['trabajador']))
		print 'Estes el el trabajador',trabajador
		producto=Producto.objects.get(id=int(request.GET['producto']))
		request.session['cliente'] = trabajador
		print "LASESSS",request.session['cliente']
		print 'ID producto',producto
		return render_to_response('producto/GuardarReserva.html',{'trabajador':trabajador,'producto':producto,'trab':trab},context_instance=RequestContext(request))

def ReservasNew(request):
	if request.method == 'POST':

		reserva = Reserva()
		reserva.id_trabajador_id = int(request.POST['trab'])
		pp = Producto.objects.get(id=int(request.POST['prod']))
		reserva.producto_id = int(request.POST['prod'])
		reserva.cantidad = int(request.POST['cant'])
		reserva.adelanto = int(0)#int(request.POST['adelanto'])
		reserva.Total = int(pp.Precio_producto) * int(request.POST['cant'])
		reserva.fecha = datetime.strptime(request.POST['fecha'],"%Y-%m-%d")
		if int(request.POST['cant'] > 0):
			reserva.save()
			lista=request.session['reserva']
			lista.append(int(reserva.id))
			request.session['reserva']=lista
			#print "este es la reserva",request.session['reserva']
			return HttpResponse("La reserva de realizó exitosamente")
		else:
			return HttpResponse("Error no puede ingresar valores Negativos.")
	else:
		return HttpResponse("GET")
def cantidadreservas(request):
	contidad=len(request.session['reserva'])
	return HttpResponse(contidad)
def get_retorna_reservas_view(request):
	productos=request.session['reserva']
	salidas=Reserva.objects.all().order_by("-id")
	out=[]
	traba=''
	precios = ''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				#return render_to_response("producto/get_retorna_salidas.html",{'aux':aux},context_instance=RequestContext(request))
				traba=j.id_trabajador
				Numcontrol+=str(j.id)+':'
	total_pago=0
	contidadPro=len(out)
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	dic={
		'pagesize':'A4',
		'Numcontrol':Numcontrol,
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'out':out,
		'total_pago':total_pago,
		'traba':traba,
		'contidadPro':contidadPro
	}
	html=render_to_string("producto/get_retorna_reservas_view.html",dic,context_instance=RequestContext(request))
	return generar_pdf(html)
def get_retorna_reservas(request):
	productos=request.session['reserva']
	salidas=Reserva.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				
				#return render_to_response("producto/get_retorna_salidas.html",{'aux':aux},context_instance=RequestContext(request))
				traba=j.id_trabajador
				Numcontrol+=str(j.id)+':'
	total_pago=0
	contidadPro=len(out)
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.now()
	dic={
		'pagesize':'A4',
		'Numcontrol':Numcontrol,
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'out':out,
		'total_pago':total_pago,
		'traba':traba,
		'contidadPro':contidadPro
	}
	return render_to_response("producto/get_retorna_reservas_view.html",dic,context_instance=RequestContext(request))
	
def RegisterReserva(request):
	if request.method == 'POST':
		print "Fechas",request.POST

	forms=FormReservas()
	return render(request, 'producto/ReservasNew.html',{'forms':forms},context_instance=RequestContext(request))
def ReservasRegistro(request):
	if request.method=='POST':
		print "jaj"
	# 	forms=FormReservas()
	# 	if forms.is_valid:
	# 		print request.POST
	# 		reserva = Reserva()
	# 		reserva.id_trabajador_id = int(request.session['cliente'])
	# 		reserva.Coutas = int(request.POST['Coutas'])
	# 		reserva.fecha_de_pago = datetime.strptime(request.POST['Fecha'],"%d/%m/%Y")
	# 		reserva.save()
	# 		rr=reserva.id
	# 		pp = Producto_Reserva()
	# 		for lis in request.session['datos']:
	# 			if int(request.session['datos'].index(lis)) % 2 == 0:
	# 				pp.cantidad = int(request.session['datos'])
	# 			else:
	# 				pp.id_producto_id = int(lis)
	# 			pp.id_reserva_id = int(rr)

				
	# 			pp.save()
	# 		#tb guardar la Informacion en la segunda tabla
	# 		return HttpResponse("Registro Exitoso")
	# 	else:
	# 		forms=FormReservas()
	# else:
	# 	forms=FormReservas()
	return render(request, 'producto/ReservasNew.html',{'forms':forms},context_instance=RequestContext(request))

def ver_reservas(request):
	reservas = Reserva.objects.all().order_by("-id")
	productos  = Producto.objects.filter(estado=0).order_by("-id")
	enbaja = Reserva.objects.filter(estado=0).count()
	enalta = Reserva.objects.filter(estado=1).count()
	tregistros = Reserva.objects.count()
	dic={
		'reservas':reservas,
		'productos':productos,
		'enbaja':enbaja,
		'enalta':enalta,
		'tregistros':tregistros
	}
	return render(request,'producto/ver_reservas.html',dic,context_instance=RequestContext(request))

def ImprimirKardexSalidas(request, id):
	salidas = SalidasPro.objects.filter(producto = int(id)).order_by("-id")
	cant = SalidasPro.objects.filter(producto = int(id)).count()
	t = 0
	c = 0
	for i in salidas:
		t = t + i.total
		c = c + i.cantidad
	dic={
		'salidas':salidas,
		'cant':cant,
		't':t,
		'c':c
	}
	return render(request,'producto/ImprimirKardexSalidas.html',dic,context_instance=RequestContext(request))
def ImprimirKardexEntradas(request, id):
	ingresos = CompraProducto.objects.filter(producto = int(id)).order_by("-id")
	cant = CompraProducto.objects.filter(producto = int(id)).count()
	t = 0
	c = 0
	for i in ingresos:
		t = t + i.total
		c = c + i.cantidad
	dic={
		'ingresos':ingresos,
		'cant':cant,
		't':t,
		'c':c
	}
	return render(request,'producto/ImprimirKardexEntradas.html',dic,context_instance=RequestContext(request))

def editReserva(request, id):
	cod = int(id)
	dato=Reserva.objects.get(id=int(id))
	if request.method == 'POST':
		forms=FormReservas(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El Registro Actualizó Correctamente")
		else:
			HttpResponse("Error al actualizar")
	else:
		forms =FormReservas(instance=dato)
	return render(request, 'producto/editReserva.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def deleteReserva(request, id):
	dato=Reserva.objects.get(id=int(id))
	return render(request,'producto/deleteReserva.html',{'dato':dato},context_instance=RequestContext(request))
def delReserva(request, id):
	if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
		Reserva.objects.filter(id=int(id)).update(estado=0)
		return HttpResponse("Se dió de Baja Al registro Correctamente.")
	else:
		return HttpResponse("Ud. no esta autenticado por favor inicie sesión")
def buscarProducto_Reserva(request):
	if request.method=="POST":
		texto = request.POST['p']
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		print "coinsidencias",resultados
		return render_to_response('producto/buscarProducto_Reserva.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET['p']
		print texto
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto_Reserva.html',{'resultados':resultados},context_instance=RequestContext(request))
def ShearProduc_Reserva(request, id):
	producto=Producto.objects.get(id=int(id))
	return render_to_response('producto/ShearProduc_Reserva.html',{'producto':producto},context_instance=RequestContext(request))

#import MySQLdb

# def KardexGeneral(request):
# 	db = MySQLdb.connect(user='root', db='almacenAnterior', passwd='', host='localhost')
# 	cursor = db.cursor()
# 	sql = cursor.execute('SELECT Nombre_producto, s.cantidad, s.Precio_unidad, s.total, i.cantidad, i.Precio_unidad, i.total from producto_salidaspro s, producto_producto pro, producto_compraproducto i WHERE pro.id = s.producto_id and pro.id = i.producto_id')
# 	names = ''
# 	for row in cursor.fetchall():
# 		print row
# 		for i in row:
# 			print i
# 	db.close()
# 	return render_to_response('producto/KardexGeneral.html', {'names': names,'sql':sql})

def KardexGeneral(request):
	fecha=datetime.now()
	dateMonthStart="%s-01-01" % (fecha.year)
	#dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month+1)[1])
	print dateMonthStart
	ingresos = CompraProducto.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha))
	salidas = SalidasPro.objects.filter(estado=0,fecha_registro__range=(dateMonthStart,fecha))
	productos = Producto.objects.filter(estado=0)
	lista = {}
	unico = []
	cantP = 0
	toP = 0
	for i in productos:
		for j in ingresos:
			for k in salidas:
				if i.id == j.producto_id  or i.id == k.producto_id:
					if i.id not in unico:
						lista[i.id] = [float(i.Stock) * float(i.Precio_producto)]
						unico.append(i.id)
						#unico.append(float(i.Stock) * float(i.Precio_producto))
	print "Unicos",lista,"********"
	primero = 0
	for i in productos:
		for j in ingresos:
			for k in salidas:
				if i.id == j.producto_id  or i.id == k.producto_id:
					primero = float(i.Stock) * float(i.Precio_producto)
					break
				break
			break
		break
	for i in productos:
		for j in unico:
			if i.id == j:
				cantP = cantP + i.Stock
				print "cantidad",cantP
				toP = toP + (float(i.Stock) * float(i.Precio_producto))
	canI = 0
	p = 0
	for i in ingresos:
		canI = canI + i.cantidad
		p = p + i.total

	canS = 0
	pS = 0
	for i in salidas:
		canS = canS + i.cantidad
		pS = pS + i.total
			
	dic={
		'ingresos':ingresos,
		'salidas':salidas,
		'productos':productos,
		'lista':lista,
		'canI':canI,
		'p':p,
		'canS':canS,
		'pS':pS,
		'cantP':cantP,
		'toP':toP,
		'primer':primero
	}
	return render(request,'producto/KardexGeneral.html',dic,context_instance=RequestContext(request))
def valorado(request):
	ingresos = CompraProducto.objects.filter(estado=0)
	salidas = SalidasPro.objects.filter(estado=0)
	productos = Producto.objects.filter(estado=0)
	lista = {}
	unico = []
	cantP = 0
	toP = 0
	for i in productos:
		for j in ingresos:
			for k in salidas:
				if i.id == j.producto_id  or i.id == k.producto_id:
					if i.id not in unico:
						lista[i.id] = [float(i.Stock) * float(i.Precio_producto)]
						unico.append(i.id)
						#unico.append(float(i.Stock) * float(i.Precio_producto))
	print "Unicos",lista,"********"
	primero = 0
	for i in productos:
		for j in ingresos:
			for k in salidas:
				if i.id == j.producto_id  or i.id == k.producto_id:
					primero = float(i.Stock) * float(i.Precio_producto)
					break
				break
			break
		break
	for i in productos:
		for j in unico:
			if i.id == j:
				cantP = cantP + i.Stock
				print "cantidad",cantP
				toP = toP + (float(i.Stock) * float(i.Precio_producto))
	canI = 0
	p = 0
	for i in ingresos:
		canI = canI + i.cantidad
		p = p + i.total

	canS = 0
	pS = 0
	for i in salidas:
		canS = canS + i.cantidad
		pS = pS + i.total
			
	dic={
		'ingresos':ingresos,
		'salidas':salidas,
		'productos':productos,
		'lista':lista,
		'canI':canI,
		'p':p,
		'canS':canS,
		'pS':pS,
		'cantP':cantP,
		'toP':toP,
		'primer':primero
	}
	html= render_to_string('producto/valorado.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)

