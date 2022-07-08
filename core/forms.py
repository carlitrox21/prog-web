from django.forms import ModelForm
from .models import *

class promoform(ModelForm):
    class Meta:
        model = promocion
        fields = [ 'nombre', 'descuento', 'idProducto']


class promonew(ModelForm):
    class Meta:
        model = promocion
        fields = [  'idpromo','nombre', 'descuento', 'idProducto']


class productoform(ModelForm):
    class Meta:
        model = Producto
        fields = [ 'NombreProducto', 'Valor', 'stock']


class productonew(ModelForm):
    class Meta:
        model = Producto
        fields = [  'IdProducto','NombreProducto', 'Valor', 'stock']






