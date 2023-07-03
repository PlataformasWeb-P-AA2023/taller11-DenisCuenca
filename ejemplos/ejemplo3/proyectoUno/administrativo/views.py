from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'index.html', informacion_template)


def obtener_estudiante(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiante = Estudiante.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiante': estudiante}
    return render(request, 'obtener_estudiante.html', informacion_template)


def crear_estudiante(request):
    """
    """
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EstudianteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante_3.html', diccionario)


def editar_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEstudiante.html', diccionario)


def eliminar_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)


def crear_numero_telefonico(request):
    """
    """

    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)


def editar_numero_telefonico(request, id):
    """
    """
    telefono = NumeroTelefonico.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST, instance=telefono)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm(instance=telefono)
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)

def crear_numero_telefonico_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoEstudianteForm(estudiante, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoEstudianteForm(estudiante)
    diccionario = {'formulario': formulario, 'estudiante': estudiante}

    return render(request, 'crearNumeroTelefonicoEstudiante.html', diccionario)
