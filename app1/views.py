from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from app1.forms import *
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'app1/inicio.html')

#def ingeniero(request):
 #   return render(request, 'app1/ingenieros.html')


# formulario ------------------------------------------------------------------------------------
def proyecto(request):

    if request.method == "POST":

        iformulario=ProyectosFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            proyecto=Proyectos(nombre=informacion["nombre"],ingenieroACargo=informacion["ingenieroACargo"], estatus=informacion["estatus"])
            proyecto.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=ProyectosFormulario()

    return render(request, 'app1/proyectos.html', {'formulario':iformulario})

# formulario ------------------------------------------------------------------------------------

def tools(request):

    if request.method == "POST":

        iformulario=ToolsFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            tools=inventario_Tools(nombre=informacion["nombre"],cantidad=informacion["cantidad"], ubicacion=informacion["ubicacion"])
            tools.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=ToolsFormulario()

    return render(request, 'app1/tools.html', {'formulario':iformulario})

# formulario ------------------------------------------------------------------------------------
def ingenieros(request):

    if request.method == "POST":

        iformulario=IngenieroFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            ingeniero=Ingenieros(nombre=informacion["nombre"],apellido=informacion["apellido"])
            ingeniero.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=IngenieroFormulario()

    return render(request, 'app1/ingenieros.html', {'formulario':iformulario})

#Busqueda de ingenieros-----------------------------------------------------------------------------------------
def buscarIngeniero(request):
    return render(request, 'app1/busquedaIngeniero.html')

def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        ingenieros=Ingenieros.objects.filter(nombre=nombre)
        return render(request, 'app1/resultadoBuscar.html', {'ingenieros': ingenieros, 'nombre': nombre})
    else:
        respuesta="No se ingresaron datos"
        return render(request, 'app1/resultadoBuscar.html', {'respuesta': respuesta})
