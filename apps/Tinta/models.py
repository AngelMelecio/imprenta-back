from django.db import models

class Tinta(models.Model):
    idTinta = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=6, null=False, blank=False)
    
    def __str__(self):
        return self.nombre