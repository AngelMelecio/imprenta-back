from django.db import models
from apps.TipoMaterial.models import TipoMaterial

# Create your models here.
class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True,auto_created=True)
    categoria = models.CharField(max_length=50, null=False, blank=False) # Papel, Cartulina, Carton, etc
    tipoMaterial = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE, null=False, blank=False)
    alto = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    ancho = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    gramaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grosor=models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f'{self.categoria} {self.tipoMaterial.nombre} {self.ancho}cm x {self.alto}cm {self.gramaje}gr  {self.color} ${self.precio}'
