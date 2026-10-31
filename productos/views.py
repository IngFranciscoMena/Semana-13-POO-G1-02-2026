from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView #, DetailView, DeleteView

## CRUD - Create, Read, Update, Delete

from .forms import ProductoForm, InventarioForm
from .models import Producto, Inventario

# Create your views here.
def inicio(request):
    return render(request, "productos/inicio/inicio.html")

## CRUD para Productos
class ProductoListView(ListView):

    model = Producto
    template_name = "productos/lista.html"
    context_object_name = "productos"

class ProductoCreateView(CreateView):

    model = Producto
    form_class = ProductoForm
    template_name = "productos/formulario.html"
    success_url = reverse_lazy("productos:lista")

class ProductoUpdateView(UpdateView):

    model = Producto
    form_class = ProductoForm
    template_name = "productos/formulario.html"
    success_url = reverse_lazy("productos:lista")

## CRUD para Inventarios
class InventarioListView(ListView):

    model = Inventario
    template_name = "productos/inventarios/lista.html"
    context_object_name = "inventarios"

class InventarioCreateView(CreateView):

    model = Inventario
    form_class = InventarioForm
    template_name = "productos/inventarios/formulario.html"
    success_url = reverse_lazy("productos:inventario_lista")