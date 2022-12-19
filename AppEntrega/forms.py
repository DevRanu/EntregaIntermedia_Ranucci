from django import forms

class AutoForm(forms.Form):
    marca= forms.CharField(label="Marca", max_length=30)
    modelo= forms.CharField(label="Modelo", max_length=30)
    anio= forms.IntegerField(label="Fabricado el año")
    airbag= forms.BooleanField(label="Tiene airbag", required=False)

class PerroForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=30)
    raza= forms.CharField(label="Raza", max_length=30)
    genero= forms.CharField(label="Macho u Hembra", max_length=6)
    edad= forms.IntegerField(label="Edad")

class EquipoForm(forms.Form):
    pais= forms.CharField(label="Pais", max_length=30)
    continente= forms.CharField(label="Continente", max_length=30)
    sigueJugando= forms.BooleanField(label="Sigue jugando?", required=False)