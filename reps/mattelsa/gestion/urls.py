from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('registrar/vehiculos', login_required(views.crear_vehiculo), name='registrar_vehiculo'),
    path('listar/vehiculos', login_required(views.listar_vehiculos), name='listar_vehiculo'),
    path('nuevo/vehiculo', login_required(views.nuevo_vehiculo), name='nuevo_vehiculo'),
    path('registro', login_required(views.registrar_ingreso), name='registrar_ingreso'),
    path('consultar/vehiculo', login_required(views.consultar_vehiculo), name='consultar_vehiculo'),
    path('consultar/ingresos', login_required(views.consultar_ingresos), name='consultar_ingresos'),
]