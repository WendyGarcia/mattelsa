from django.contrib import admin

# Register your models here.
from .models import TipoDocumento, Cliente, TipoVehiculo, Vehiculo, Celda, Registro


admin.site.register(TipoDocumento)
admin.site.register(Cliente)
admin.site.register(TipoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Celda)
admin.site.register(Registro)