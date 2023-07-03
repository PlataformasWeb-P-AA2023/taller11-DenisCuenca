"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_estudiante, 
            name='obtener_estudiante'),
        path('crear/estudiante', views.crear_estudiante, 
            name='crear_estudiante'),
        path('editar_estudiante/<int:id>', views.editar_estudiante, 
            name='editar_estudiante'),
        path('eliminar/estudiante/<int:id>', views.eliminar_estudiante, 
            name='eliminar_estudiante'),
        # numeros telefonicos
        path('crear/numero/telefonico', views.crear_numero_telefonico, 
            name='crear_numero_telefonico'),
        path('editar/numero/telefonico/<int:id>', views.editar_numero_telefonico, 
            name='editar_numero_telefonico'),
        path('crear/numero/telefonico/estudiante/<int:id>', 
            views.crear_numero_telefonico_estudiante, 
            name='crear_numero_telefonico_estudiante'),
 ]
