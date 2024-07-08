from django import forms
from .models import Genero, Producto, Carrito, Trabajo
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ["genero"]
        labels = {'genero':'Género'}
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['usuario', 'producto', 'cantidad']

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['titulo', 'descripcion', 'mecanico', 'fecha_inicio', 'fecha_fin']
