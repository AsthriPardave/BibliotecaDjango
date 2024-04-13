from django.db import models

# Create your models here.
class Autor(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    nacimiento = models.IntegerField(null=True, blank=True)
    fallecimiento = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.apellido

class Cliente(models.Model):
    apellido = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=15)
    direccion_postal = models.CharField(max_length=150)

class MetodoPago(models.Model):
    metodo_pago = models.CharField(max_length=30)

class Calificacion(models.Model):
    calificacion = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.calificacion

class Editora(models.Model):
    editora = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.editora

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()
    edicion = models.CharField(max_length=30)
    costo = models.FloatField()
    precio_venta_sugerido = models.FloatField()
    disponible = models.BooleanField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, null=True, blank=True)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
            return self.titulo

class Puesto(models.Model):
    puesto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

class Empleado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

class EstadoOrden(models.Model):
    estado = models.CharField(max_length=30)

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    monto_venta = models.FloatField()
    fecha_orden = models.DateField()
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    fecha_despacho = models.DateField(null=True, blank=True)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estado_orden = models.ForeignKey(EstadoOrden, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.pk
    
class LibroAutor(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.libro + self.autor

class LibroOrden(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.libro + self.orden