from django.urls import path

from .views import (
    ## CRUD para Productos
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ## CRUD para Inventarios
    InventarioListView,
    InventarioCreateView,
    InventarioUpdateView,
    InventarioDeleteView
)

app_name = "productos"

urlpatterns = [
    ### CRUD para Productos
    path("", ProductoListView.as_view(), name="lista"),
    path("nuevo/", ProductoCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", ProductoUpdateView.as_view(), name="editar"),
    path("eliminar/<int:pk>", ProductoDeleteView.as_view(), name="eliminar"),
    ### CRUD para Inventarios
    path("inventario/", InventarioListView.as_view(), name="inventario_lista"),
    path("inventario/nuevo", InventarioCreateView.as_view(), name="inventario_crear"),
    path("inventario/editar/<int:pk>", InventarioUpdateView.as_view(), name="inventario_editar"),
    path("inventario/eliminar/<int:pk>", InventarioDeleteView.as_view(), name="inventario_eliminar"),

]