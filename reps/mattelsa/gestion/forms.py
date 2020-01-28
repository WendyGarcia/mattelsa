from django import forms

from . import models

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = models.Vehiculo
        fields = ('cliente','cilindraje','tiempos','placa','modelo','puertas','foto','tipo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].required = False
        self.fields['cliente'].widget = forms.HiddenInput()





class ClienteForm(forms.ModelForm):


    class Meta:
        model = models.Cliente 
        fields = ('nombre', 'documento', 'tipo_documento' )

class RegistroForm(forms.ModelForm):
    class Meta:
        model = models.Registro
        fields = ('vehiculo', 'celda', 'fecha')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)