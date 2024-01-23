from django.db import models
from apps.Prensa.models import Prensa
from apps.Tinta.models import Tinta
from apps.TipoImpresion.models import TipoImpresion

class PrecioPrensa(models.Model):
    idPrecioPrensa = models.AutoField(auto_created=True, primary_key=True)
    prensa = models.ForeignKey(Prensa, on_delete=models.CASCADE)
    precioColor = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    precioCantidad = models.DecimalField(max_digits=10, decimal_places=2)
    tinta = models.ForeignKey(Tinta, on_delete=models.CASCADE)
    tipoImpresion = models.ForeignKey(TipoImpresion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prensa.nombre} - {self.tinta.nombre} - {self.tipoImpresion.nombre} - {self.cantidad} - ${self.precioCantidad}'