from django.db import models

# Create your models here.

class Edificio(models.Model):
    op = (('residencial', 'residencial'), ('comercial', 'comercial'))
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=op)

    def __str__(self):
        return f"{self.nombre}, {self.tipo}" 
    
    def obtener_num_cuartos(self):
        # valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        # valor = sum(valor)  # [10.2, 20]
        valor = 0
        for t in self.departamentos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.num_cuartos
        return valor

    def obtener_total(self):
        """
        """
        valor = 0.0
        for t in self.departamentos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.costo
        return valor

    


class Departamento(models.Model):
    op = (('residencial', 'residencial'), ('comercial', 'comercial'))
    nombre_propietario = models.CharField(max_length=250)
    costo = models.FloatField()
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name="departamentos")
    

    def __str__(self):
        return self.nombre_propietario
    
    


