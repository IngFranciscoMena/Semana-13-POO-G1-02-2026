from django.db.models import ProtectedError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

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


class ProductoDeleteView(DeleteView):

    model = Producto
    template_name = "productos/confirmar_eliminar.html"
    success_url = reverse_lazy("productos:lista")

    def form_valid(self, form):
        try:
            self.object.delete()            
        except ProtectedError:
            messages.error(
                self.request,
                "No se puede eliminar el producto porque tiene registros de inventario asociados."
            )
            return HttpResponseRedirect(self.get_success_url())
        
        return HttpResponseRedirect(self.get_success_url())
    

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

class InventarioUpdateView(UpdateView):

    model = Inventario
    form_class = InventarioForm
    template_name = "productos/inventarios/formulario.html"
    success_url = reverse_lazy("productos:inventario_lista")

class InventarioDeleteView(DeleteView):

    model = Inventario
    template_name = "productos/inventarios/confirmar_eliminar.html"
    success_url = reverse_lazy("productos:inventario_lista")