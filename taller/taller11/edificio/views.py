from django.shortcuts import redirect, render
from .models import Departamento, Edificio
from .form import DepartamentoForm, EdificioForm
# Create your views here.

def list_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'edificio/list_departamentos.html', {'departamentos': departamentos})

def list_edificios(request):
    edificios = Edificio.objects.all()
    
    return render(request, 'edificio_list.html', {'edificios': edificios,  })

def edificio_create(request):
    if request.method == 'POST':
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_edificios)
    else:
        form = EdificioForm()
    return render(request, 'edificio_form.html', {'formulario': form})

def edificio_edit(request, id):
    e = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        form = EdificioForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect(list_edificios)
    else:
        form = EdificioForm(instance=e)
    return render(request, 'edificio_form.html', {'formulario': form})

def eliminar_edificio(request, id):
    """
    """
    e = Edificio.objects.get(pk=id)
    e.delete()
    return redirect(list_edificios)



def departamento_create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_edificios)
    else:
        form = DepartamentoForm()
    return render(request, 'departamento_form.html', {'formulario': form})

def departamento_edit(request, id):
    e = Departamento.objects.get(pk=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect(list_edificios)
    else:
        form = DepartamentoForm(instance=e)
    return render(request, 'departamento_form.html', {'formulario': form})

def eliminar_departamento(request, id):
    """
    """
    e = Departamento.objects.get(pk=id)
    e.delete()
    return redirect(list_edificios)
