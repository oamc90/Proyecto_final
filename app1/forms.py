from django import forms

class IngenieroFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    cargo=forms.CharField(max_length=50)
    proyecto=forms.CharField(max_length=50)

class ProyectosFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    ingenieroACargo=forms.CharField(max_length=50)
    estatus=forms.CharField(max_length=50)


class ToolsFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    ubicacion=forms.CharField(max_length=50)