from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ('id','apellido','nombre','nacimiento')
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','apellido','telefono')
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id','metodo_pago')
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id','calificacion')
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id','editora')
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','costo','disponible')
class PuestoAdmin(admin.ModelAdmin):
    list_display = ('id','puesto')
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido','puesto')
class EstadoOrdenAdmin(admin.ModelAdmin):
    list_display = ('id','estado')
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','monto_venta','metodo_pago','estado_orden')

# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(MetodoPago, MetodoPagoAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Puesto, PuestoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(EstadoOrden, EstadoOrdenAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(LibroOrden)
admin.site.register(LibroAutor)
