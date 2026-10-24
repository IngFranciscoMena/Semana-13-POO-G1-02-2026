from django.db import models

# Create your models here.
class Producto(models.Model):

    # crear nuestro atributos de clase
    nombre = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre