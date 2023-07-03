from django.urls import path
from .views import list_departamentos, list_edificios

urlpatterns = [
    path("edificios", list_edificios, name="list_edificios"),
    path("departamentos", list_departamentos, name="list_departamentos"),
]