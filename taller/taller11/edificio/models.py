from django.db import models

# Create your models here.

class Edificio(models.Model):
    op = (('residencial', 'residencial'), ('comercial', 'comercial'))
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=op)

    def __str__(self):
        return self.nombre
    


class Departamento(models.Model):
    op = (('residencial', 'residencial'), ('comercial', 'comercial'))
    nombre_propietario = models.CharField(max_length=250)
    costo = models.FloatField()
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name="departamentos")
    

    def __str__(self):
        return self.nombre_propietario
    
    


