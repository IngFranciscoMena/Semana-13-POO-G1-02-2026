from django import forms
from .models import Producto, Inventario

class ProductoForm(forms.ModelForm):

    ## __init__
    class Meta:
        model = Producto
        fields = [
            "nombre",
            "precio",
            "descripcion"
        ]

class InventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = [
            "producto",
            "cantidad",
            "ubicacion",
            "stock_minimo"            
        ]

