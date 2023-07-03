from django.shortcuts import render
from .models import Departamento, Edificio
# Create your views here.

def list_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'edificio/list_departamentos.html', {'departamentos': departamentos})

def list_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'edificio_list.html', {'edificios': edificios})