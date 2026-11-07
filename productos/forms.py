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

        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio del producto",
            "descripcion": "Descripción del producto"
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Teclado Mecánico"
                }),
            "precio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 49.99",
                    "step": "0.01",
                    "min": "0"
                }),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Ej. Teclado mecánico con retroiluminación RGB",
                    "rows": 3
                }),
        }
        

class InventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario

        fields = [
            "producto",
            "cantidad",
            "ubicacion",
            "stock_minimo"
        ]

        labels = {
            "producto": "Seleccionar producto",
            "cantidad": "Cantidad disponible",
            "ubicacion": "Ubicación del producto",
            "stock_minimo": "Stock mínimo"
        }

        widgets = {
            "producto": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "cantidad": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "placeholder": "Ej. 20"
                }
            ),

            "ubicacion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Bodega principal"
                }
            ),

            "stock_minimo": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "placeholder": "Ej. 5"
                }
            )
        }

