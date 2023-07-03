from django.forms import ModelForm
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
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor    
