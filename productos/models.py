from django.db import models

# Create your models here.
class Producto(models.Model):

    # crear nuestro atributos de clase
    nombre = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):

    cantidad = models.PositiveIntegerField(default=0)
    ubicacion = models.CharField(max_length=100, default="Bodega principal")
    stock_minimo = models.PositiveBigIntegerField(default=5)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="inventarios"
    )

    def __str__(self):
        return f""


    ## Producto Laptop, Teclado, Mouse

    ## Inventario: Laptop 10 existencias en la Bodega principal
    ##              Laptop 5 existencias en la Bodega secundaria
    ## ....

    # Fecha_Registro Datetime Not Null default getdate()