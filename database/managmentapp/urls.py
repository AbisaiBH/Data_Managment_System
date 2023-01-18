from django.urls import path
from . import views

urlpatterns = [
    path('',views.empleados, name="Interface"),
    path('new',views.empleados_new, name="Nuevo_Empleado"),
]