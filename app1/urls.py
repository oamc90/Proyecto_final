from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ingenieros/',ingenieros, name='ingeniero'),
    path('proyectos/',proyecto, name='proyecto'),
    path('tools/',tools, name='tools'),
   # path('ingenierosFormulario/',ingenierosFormulario, name='ingenierosFormulario'),
    path('busquedaIngeniero/',buscarIngeniero, name='busquedaIngeniero'),
    path('buscar/',buscar, name='buscar'),
    
]

