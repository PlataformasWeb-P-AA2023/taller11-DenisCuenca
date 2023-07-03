# Taller 11 (Laboratorio) 
## Creación de proyectos de ambiente web a través del framework Django. Usar herencia de plantillas.

### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]
	
* Departamento
	* nombre completo del propietario
	* costo del departamento
	* número de cuartos
	* edificio
	
Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite
- Lenguaje Python
- Framework Django
- https://datatables.net/

### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto den Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- Generar procesos que permitan Ingresar, editar, eliminar datos a las entidades.
- Generar una vista que liste los edificios - usar datatables:
	- Por cada edificio presentar: nombre, dirección, ciudad, tipo, listado de departamentos, **número total de cuartos del edificio, costo total de los departamentos del edificio**.
- Usar herencia de plantillas, hojas de estilo
- Usar formularios creados desde el archivo forms.py
 	- Agregar validaciones: 
 		- Costo de un departamento no puede ser mayor a $100 mil.
 		- Número de cuartos no puede ser 0, ni mayor a 7
 		- El nombre de la ciudad no puede iniciar con la letra mayúscula **L**
 		- El nombre completo de un propietario **no** debe tener menos de 3 palabras.

