#encoding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from mipagina.apps.producto.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from django.db.models import Q
from .forms import *
import datetime
import calendar
# Create your views here.
def NewClient(request):
	if request.method=='POST':
		forms=FormTrabajador(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormTrabajador()
	return render_to_response('cliente/NewClient.html',{'forms':forms},context_instance=RequestContext(request))

def VerClientes(request):
    datos=Trabajador.objects.all().order_by('-id')
    cliente=Trabajador.objects.filter(estado=0).count()
    return render_to_response('cliente/VerClientes.html',{'datos':datos,'cliente':cliente},context_instance=RequestContext(request))

def buscar(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        texto=request.POST["q"]
        busqueda=(
            Q(Nombre_trabajador__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Trabajador.objects.filter(busqueda).distinct()
        print "Clente:",resultados
        return render_to_response('cliente/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

    else:
        texto=request.GET["q"]
        busqueda=(
            Q(Nombre_trabajador__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Trabajador.objects.filter(busqueda).distinct()
        # html="<ul class='ul_lista'>"
        # for i in resultados:
        #     html=html+"<li><a href='/detalles/"+str(i.id)+"/'>"+i.Nombre_trabajador+""+i.Apellidos+"</a></li>"
        # html=html+"<ul>"
        return render_to_response('cliente/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

def deleteTrabajador(request, id):
    dato=Trabajador.objects.get(id=int(id))
    return render_to_response('cliente/deleteTrabajador.html',{'dato':dato},context_instance=RequestContext(request))
def delTrabajador(request, id):
    Trabajador.objects.filter(id=int(id)).update(estado=1)
    return HttpResponse("Se dió de Baja Al registro Correctamente.")
def editTrabajador(request, id):
    cod=int(id)
    dato=Trabajador.objects.get(id=int(id))
    if request.method=='POST':
        forms=FormTrabajador(request.POST, instance=dato)
        if forms.is_valid():
            forms.save()
            return HttpResponse("El registro se actualizó correctamente")
    else:
        forms=FormTrabajador(instance=dato)
    return render_to_response('cliente/editTrabajador.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))

def escogido(request,id):
    persona=Trabajador.objects.get(id=int(id))
    fecha=datetime.datetime.now()
    dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
    #la linea de abajo Consultamos todas las selidas q el cliente realizo con el MES 
    ventas=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart, estado=0).order_by("-id")
    pagado=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart, estado=0).order_by("-id")
    totaoPagado=0
    cont=0
    for p in pagado:
        totaoPagado += p.total
        cont = cont + 1
    reservas=Reserva.objects.filter(id_trabajador=int(id), fecha_registro__gte=dateMonthStart, estado=1).order_by('-id')
    productos=Producto.objects.filter(estado=0).order_by('id')
    #cont=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart, estado=0).count()
    dic={
        'ventas':ventas,
        'cont':cont,
        'persona':persona,
        'totaoPagado':totaoPagado,
        'reservas':reservas,
        'productos':productos
    }
    return render_to_response('cliente/escogido.html',dic,context_instance=RequestContext(request))
def deleteSalidasRecuperar(request, id):
    if request.user.is_superuser and request.user.is_staff and request.user.is_active:
        SalidasPro.objects.filter(id=int(id)).update(estado=0)
        return HttpResponse("El registro a sido dado de Alta Nuevamente.")
    else:
        return HttpResponse("Ud. no puede seralizar esta operación.")
def deleteIngresosRecuperar(request, id):
    if request.user.is_superuser and request.user.is_staff and request.user.is_active:
        CompraProducto.objects.filter(id=int(id)).update(estado=0)
        return HttpResponse("El registro a sido dado de Alta Nuevamente.")
    else:
        return HttpResponse("Ud. no puede seralizar esta operación.")

def portada(request):
    if 'trabajador' in request.session:
        trabajador = request.session['trabajador']
        return render(request,'cliente/portada.html',{'trabajador':trabajador},context_instance=RequestContext(request))
    else:
        return render(request,'cliente/portada.html',context_instance=RequestContext(request))
def prodcutos_Reserva(request):
    productos = Producto.objects.filter(estado=0).order_by("-id")[0:9];
    dic={
        'productos':productos
    }
    return render(request,'cliente/prodcutos_Reserva.html',dic,context_instance=RequestContext(request))
def cliente_reserva(request, id):
    producto = Producto.objects.get(id=int(id))
    dic={
        'producto':producto
    }
    return render(request,'cliente/cliente_reserva.html',dic,context_instance=RequestContext(request))
def reserva_cli(request, id):
    cod = int(id)
    if 'trabajador' in request.session:
    #si esta logoado el cliente
        cantidad = int(request.GET['cantidad'])
        if cantidad < 1:
            cantidad = 1
        #aki guardar la reserva del cliente
        print "la Cantidad",cantidad
        trabajador = request.session['trabajador']
        return render(request,'cliente/mensaje.html',{'trabajador':trabajador,'cantidad':cantidad},context_instance=RequestContext(request))
        #return HttpResponse("Felicidades %s Ingresaste tus datos al sistema, pero lamentamos informarle que las compras online aún no se estan realizando, pero ya teniendo tus datos de ofresemos un descuento por cuanquiera de nuestros productos cuando pase por nuestra tienda. estamos para servirle comentenos mas abajo que le a parecido nuestra iniciativa de la tienda Online gracias hasta pronto."%(request.session['trabajador']))
    else:    
        if request.method=='POST':
            forms=FormTrabajador(request.POST)
            if forms.is_valid():
                forms.save()
                return HttpResponse("Bien tus datos se ha registrado correctamente")
        else:
            forms=FormTrabajador()
        return render(request,'cliente/reserva_cli.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def loguinCliente(request):
    if request.method == 'POST':
        forms = TrabajadorLoguin(request.POST)
        if forms.is_valid():
            tel = request.POST['tel']
            ci = request.POST['ci']
            try:
                dato = Trabajador.objects.get(Ci_Nit=int(ci), Telefono=int(tel))
                print dato
                if dato.Ci_Nit == int(request.POST['ci']) and dato.Telefono == int(request.POST['tel']):
                    request.session['trabajador'] = dato.Nombre_trabajador#guardo el nombre del trabajador
                    request.session['id_trabajador'] = dato.id#Guardo el Id del CLiente
                    trabajador = request.session['trabajador']
                    print "Ingresaste al Sistema"
                    #return redirect('/portada/?p=%s' % trabajador )
                    return HttpResponse("bien")
                    #return render(request,'cliente/portada.html',{'trabajador':trabajador},context_instance=RequestContext(request))
                else:
                    return HttpResponse("Error... Datos Incorrectos. Intente Nuevamente")
            except Trabajador.DoesNotExist:
                return HttpResponse("Los datos no son válidos Intente Nuevamente")
    else:
        forms=TrabajadorLoguin()
    return render(request,'cliente/loguinCliente.html',{'forms':forms},context_instance=RequestContext(request))
def logoutCliente(request):
    try:
        del request.session['trabajador']
    except KeyError:
        pass
    return HttpResponseRedirect('/portada/')