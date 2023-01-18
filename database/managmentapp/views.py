from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Empleados
from .forms import Empleado_form

@login_required
def empleados(request):
    empleados = Empleados.objects.all()
    return render(request, "interface.html", {'empleados':empleados})

def empleados_new(request):
    empleados = Empleados.objects.all()
    if request.method == "POST":
        form = Empleado_form(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('Interface')
    else:
        form = Empleado_form()
        return render(request, "forum.html",{'form':form, 'empleados':empleados})
