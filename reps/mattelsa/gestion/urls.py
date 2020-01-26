from django.urls import path
from . import views



urlpatterns = [
    path('registrar/vehiculos', views.crear_vehiculo, name='registrar_vehiculo'),
    path('listar/vehiculos', views.listar_vehiculos, name='listar_vehiculo'),
    path('nuevo/vehiculo', views.nuevo_vehiculo, name='nuevo_vehiculo'),
    path('registro', views.registrar_ingreso, name='registrar_ingreso'),
    path('consultar/vehiculo', views.consultar_vehiculo, name='consultar_vehiculo'),
    path('consultar/ingresos', views.consultar_ingresos, name='consultar_ingresos'),
]