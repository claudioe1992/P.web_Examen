from django.contrib import admin
from .models import Genero, Mecanico, Producto, Carrito, Trabajo
# Register your models here.

admin.site.register(Genero)
admin.site.register(Mecanico)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Trabajo)