from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    nombre = models.CharField('Nombre', max_length=200)


    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    documento = models.CharField('Documento', max_length=200)
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name='Tipo documento', on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=200)


    def __str__(self):
        return self.nombre


class TipoVehiculo(models.Model):
    nombre = models.CharField('Nombre', max_length=200)


    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='cliente', on_delete=models.CASCADE)
    cilindraje = models.CharField('Cilindraje', max_length=200, null=True, blank=True)
    tiempos = models.CharField('Tiempos', max_length=200, null=True, blank=True)
    placa = models.CharField('Placa', max_length=200)
    modelo = models.CharField('Modelo', max_length=200, null=True, blank=True)
    puertas = models.IntegerField('Puertas', null=True, blank=True)    
    foto = models.FileField('Foto', null=True, blank=True)
    tipo = models.ForeignKey(TipoVehiculo, verbose_name='Tipo vehiculo', on_delete=models.CASCADE)



    def __str__(self):
        return self.placa


class Celda(models.Model):
    numero = models.IntegerField('Numero')
    descripcion = models.CharField('Nombre', max_length=200)


    def __str__(self):
        return self.descripcion


class Registro(models.Model):

    vehiculo = models.ForeignKey(Vehiculo, verbose_name='Vehiculo', on_delete=models.CASCADE)
    celda = models.ForeignKey(Celda, verbose_name='Celda', on_delete=models.CASCADE)
    Fecha = models.DateTimeField('Fecha ingreso')