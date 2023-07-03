from django.urls import path
from .views import list_departamentos, list_edificios, edificio_create, edificio_edit, eliminar_edificio, departamento_edit, departamento_create, eliminar_departamento

urlpatterns = [
    path("edificios", list_edificios, name="list_edificios"),
    path("departamentos", list_departamentos, name="list_departamentos"),


    path("create/edificio", edificio_create, name="edificio_create"),
    path("edit/edificio/<int:id>", edificio_edit, name="edificio_edit"),
    path('eliminar/edificio/<int:id>', eliminar_edificio, 
            name='eliminar_ed'),


    path("create/departamento", departamento_create, name="departamento_create"),
    path("edit/departamento/<int:id>", departamento_edit, name="departamento_edit"),
    path('eliminar/departamento/<int:id>', eliminar_departamento, 
            name='eliminar_departamento'),


]