from operator import index
from turtle import home
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
     path('', index, name="index"),
     path('registrarse', registrarse, name="registrarse"),
     path('suscribirse', suscribirse, name="suscribirse"),
     path('tienda', tienda, name="tienda"),
     path('carrito', carrito, name="carrito"),
     path('historial', historial, name="historial"),
     path('crud', crud, name="crud"),
     path('modificarSuscriptor/<id>', modificarSuscriptor , name="modificarSuscriptor"),
     path('eliminarPromocion/<id>', eliminarPromocion , name="eliminarPromocion"),
     path('crear_promocion', crear_promocion , name="crear_promocion"),
     path('crud_productos', crud_productos, name="crud_productos"),
     path('modificar_Producto/<id>', modificar_Producto , name="modificar_Producto"),
     path('crear_producto', crear_producto , name="crear_producto"),
     path('eliminarProducto/<id>', eliminarProducto , name="eliminarProducto"),
     path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
     path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
     
]
