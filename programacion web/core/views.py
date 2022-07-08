from distutils import core
from .models import *
from .forms import promoform
from .forms import promonew
from .forms import productoform
from .forms import productonew
from django .shortcuts import redirect, render 
from django.contrib.auth.forms import UserCreationForm

def index (request):
    return render (request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def suscribirse (request):
    return render (request, 'core/suscribirse.html')

def tienda (request):
    return render (request, 'core/tienda.html')  

def carrito (request):
    return render (request, 'core/carrito.html')    

def historial (request):
    return render (request, 'core/historial.html')       

def crud (request):
    contexto = {'promocion': promocion.objects.all()}
    return render (request, 'core/crud.html', contexto)    

def modificarSuscriptor(request, id):
    Sub = promocion.objects.get(idpromo=id)
    datos = {"form":promoform(instance=Sub)}
    if request.method == "POST":
        form = promoform(request.POST, instance=Sub)
        if form.is_valid:
            form.save()
            
            datos["mensaje"] = "suscriptor modificado!."
            datos['form'] = form
            return redirect (to= "index")
            
    return render(request, 'core/modificar_suscriptores.html', datos)

def eliminarPromocion(request, id):
    vehiculo = promocion.objects.get(idpromo=id)
    vehiculo.delete()
    return redirect(to="index")

def crear_promocion(request):
    datos = {"form":promonew()}
    if request.method == "POST":
        form = promonew(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
            return redirect (to= "index")
    return render(request, 'core/crear_promocion.html', datos)



def crud_productos (request):
    contexto = {'producto': Producto.objects.all()}
    return render (request, 'core/crud_productos.html', contexto)   

def modificar_Producto(request, id):
    Sub = Producto.objects.get(IdProducto=id)
    datos = {"form":productoform(instance=Sub)}
    if request.method == "POST":
        form = productoform(request.POST, instance=Sub)
        if form.is_valid:
            form.save()
            
            datos["mensaje"] = "suscriptor modificado!."
            datos['form'] = form
            return redirect (to= "index")

    return render(request, 'core/modificar_producto.html', datos)

def eliminarProducto(request, id):
    vehiculo = Producto.objects.get(IdProducto=id)
    vehiculo.delete()
    return redirect(to="index")


def crear_producto(request):
    datos = {"form":productonew()}
    if request.method == "POST":
        form = productonew(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
            return redirect (to= "index")
    return render(request, 'core/crear_producto.html', datos)



def registrarse(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(to="login")
    else:
        return render(request, 'core/registrarse.html', {'form':UserCreationForm()})