from django.urls import path

from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    InventarioListView,
    InventarioCreateView
)

app_name = "productos"

urlpatterns = [
    path("", ProductoListView.as_view(), name="lista"),
    path("nuevo/", ProductoCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", ProductoUpdateView.as_view(), name="editar"),
    path("inventario/", InventarioListView.as_view(), name="inventario_lista"),
    path("inventario/nuevo", InventarioCreateView.as_view(), name="inventario_crear")
]