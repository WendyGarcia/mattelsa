from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from . import forms




def listar_vehiculos(request):

    
    vehiculos = models.Vehiculo.objects.all()

    return render(request, 'gestion/lista_vehiculos.html',{'vehiculos':vehiculos})


def nuevo_vehiculo(request):
    form = forms.VehiculoForm()
    form_cliente = forms.ClienteForm()
    tipo_vehiculo = models.TipoVehiculo.objects.all()
    tipo_documento = models.TipoDocumento.objects.all()
    return render(request, 'gestion/crear_vehiculos.html',{'tipo_vehiculo':tipo_vehiculo,
                                                        'tipo_documento':tipo_documento,
                                                     'form_cliente':form_cliente})


def crear_vehiculo(request):
    try:

        try:
            cliente = models.Cliente.objects.get(documento = request.POST['documento'])

            form_vehiculo = forms.VehiculoForm(request.POST)
            if form_vehiculo.is_valid():
                nuevo_cliente = form_vehiculo.save(commit=False)
                nuevo_cliente.cliente = cliente
                nuevo_cliente.save()

        except models.Cliente.DoesNotExist:

            form_cliente = forms.ClienteForm(request.POST)
            if form_cliente.is_valid():
                form_cliente.save()

            form_vehiculo = forms.VehiculoForm(request.POST)
            if form_vehiculo.is_valid():
                nuevo_cliente = form_vehiculo.save(commit=False)
                nuevo_cliente.cliente = form_cliente.instance
                nuevo_cliente.save()

        messages.success(request, "Vehiculo creado correctamente")
    except:

        messages.warning(request, "Ocurrio un error, por favor intente nuevamente")

    return render(request, 'gestion/lista_vehiculos.html',{})

def registrar_ingreso(request): 
    if request.POST:
        try:
            registro = forms.RegistroForm(request.POST)
            if registro.is_valid():
                registro.save()

                models.Celda.objects.update(ocupada = True)

            form = forms.RegistroForm
            messages.success(request, "Ingreso creado correctamente")

            return render(request, 'gestion/registro.html',{'form':form})
        except:
            form = forms.RegistroForm
            messages.warning(request, "Ocurrio un error, por favor intente nuevamente")
            return render(request, 'gestion/registro.html',{'form':form})
    else:
        
        form = forms.RegistroForm
        celdas = models.Celda.objects.all()
    
        return render(request, 'gestion/registro.html',{'celdas':celdas})

def consultar_vehiculo(request):
    if request.POST['documento']:
        try:
            cliente = models.Cliente.objects.get(documento = request.POST['documento'])
            vehiculos = models.Vehiculo.objects.filter(cliente = cliente.id)
            celdas = models.Celda.objects.filter(ocupada = False)

            return render(request, 'gestion/registro.html',{'vehiculos':vehiculos, 'celdas': celdas})
        except models.Cliente.DoesNotExist:
            messages.warning(request, "El cliente no se encuentra registrado")
            return redirect("nuevo_vehiculo")

    if request.POST['placa']:
        try:
            vehiculos = models.Vehiculo.objects.get(placa = request.POST['placa'])
            celdas = models.Celda.objects.filter(ocupada = False)
    
            return render(request, 'gestion/registro.html',{'vehiculos':vehiculos, 'celdas': celdas})
        except models.Vehiculo.DoesNotExist:
            messages.warning(request, "El vehiculo no se encuentra registrado")
            return redirect("nuevo_vehiculo")


def consultar_ingresos(request): 
    if request.POST:

        clientes = models.Cliente.objects.filter(documento = request.POST['documento']).values_list('id', flat=True)
        vehiculos = models.Vehiculo.objects.filter(cliente__in = clientes).values_list('id', flat=True)
        ingresos = models.Registro.objects.filter(vehiculo__in = vehiculos)

    else:
        ingresos = models.Registro.objects.all()
    
    return render(request, 'gestion/informe.html',{'ingresos':ingresos})
        