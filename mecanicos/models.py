from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.genero)
    
class Mecanico(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero', related_name='mecanicos')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    stock = models.PositiveIntegerField()  # Cantidad disponible en stock
    fecha_agregado = models.DateTimeField(auto_now_add=True)  # Fecha en que el producto fue agregado

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    agregado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100)  # Título del trabajo
    descripcion = models.TextField()  # Descripción del trabajo
    mecanico = models.ForeignKey('Mecanico', on_delete=models.CASCADE, related_name='trabajos')  # Mecánico que realizó el trabajo
    fecha_inicio = models.DateTimeField()  # Fecha de inicio del trabajo
    fecha_fin = models.DateTimeField()  # Fecha de finalización del trabajo

    def __str__(self):
        return self.titulo

