from django.forms import ModelForm
from django import forms
from .models import Departamento, Edificio
from django.utils.translation import gettext_lazy as _

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = "__all__"
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'tipo': _('Ingrese tipo por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
        }
    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        

        if valor[0] == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return valor      



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = "__all__"
        labels = {
            'nombre_propietario': _('Ingrese nombre por favor'),
            'costo': _('Ingrese csoto por favor'),
            'numero de cuartos': _('Ingrese el numero por favor'),
            'edificio': _('Ingrese edificio por favor'),
        }

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        

        if valor < 100.000:
            raise forms.ValidationError("Costo de un departamento no puede ser mayor a $100 mil.")
        return valor  
    
    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        

        if valor < 0 or valor > 7:
            raise forms.ValidationError("Número de cuartos no puede ser 0, ni mayor a 7.")
        return valor  
    
    def clean_nombre_propietario(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())
        """
        """

        if num_palabras < 3:
            raise forms.ValidationError("El nombre completo de un propietario no debe tener menos de 3 palabras.")
        return valor
    
    


