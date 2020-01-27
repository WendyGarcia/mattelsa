from django.shortcuts import render
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
    import pdb; pdb.set_trace()

    try:
        cliente = models.Cliente.objects.get(documento = request.POST['documento'])

        form_vehiculo = forms.VehiculoForm(request.POST)
        if form_vehiculo.is_valid():
            form_vehiculo['cliente'] = cliente
            form_vehiculo.save()

    except models.Cliente.DoesNotExist:

        form_cliente = forms.ClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()

        form_vehiculo = forms.VehiculoForm(request.POST, form_cliente.instance)
        if form_vehiculo.is_valid():
            form_vehiculo.save()


    return render(request, 'gestion/lista_vehiculos.html',{})

def registrar_ingreso(request): 
    if request.POST:
        registro = forms.RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()

        form = forms.RegistroForm
        return render(request, 'gestion/registro.html',{'form':form})
    else:
        form = forms.RegistroForm
    
        return render(request, 'gestion/registro.html',{'form':form})

def consultar_vehiculo(request):
    if request.POST['documento']:

        cliente = models.Cliente.objects.get(documento = request.POST['documento'])
        vehiculos = models.Vehiculo.objects.filter(cliente = cliente.id)
        celdas = models.Celda.objects.all()

        return render(request, 'gestion/registro.html',{'vehiculos':vehiculos, 'celdas': celdas})

    if request.POST['placa']:

        vehiculos = models.Vehiculo.objects.filter(placa = request.POST['placa'])
        celdas = models.Celda.objects.all()
 
        return render(request, 'gestion/registro.html',{'vehiculos':vehiculos, 'celdas': celdas})


def consultar_ingresos(request): 
    import pdb; pdb.set_trace()
    if request.POST:

        clientes = models.Cliente.objects.filter(documento = request.POST['documento']).values_list('id', flat=True)

        vehiculos = models.Vehiculo.objects.filter(cliente__in = clientes).values_list('id', flat=True)

        ingresos = models.Registro.objects.filter(vehiculo__in = vehiculos)


        return render(request, 'gestion/informe.html',{'ingresos': ingresos })
    else:
        ingresos = models.Registro.objects.all()
    
        return render(request, 'gestion/informe.html',{'ingresos':ingresos})
        