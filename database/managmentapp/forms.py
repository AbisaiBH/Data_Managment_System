from django import forms

from .models import Empleados

class Empleado_form(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('__all__')