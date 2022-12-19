from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
import datetime
from .models import Auto, Perro, Equipo
from django.urls import reverse_lazy
from .forms import AutoForm, PerroForm, EquipoForm
#   from AppEntrega.forms import Autoform, PerroForm, EquipoForm



def inicio(request):
    return render(request, "inicio.html")

def categorias(request):
    return render(request, "categorias.html")

#          #          #          #          #          #          #          #          
#          AUTOS
#          #          #          #          #          #          #          #  

def listaAutos(request):
    autos= Auto.objects.all()
    return render(request, "autos.html", {"autos": autos})

def addAuto(request):
    if request.method=="POST":
        form= AutoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            auto= Auto(marca=info["marca"], modelo=info["modelo"], anio=info["anio"], airbag=info["airbag"])
            auto.save()
            autos= Auto.objects.all()
            return render(request, "autos.html", {"autos": autos})
        else:
            return render(request, "formautos.html", {"form": form, "mensaje": "Algo malió sal."})
    else:
        form= AutoForm()
        return render(request, "formautos.html", {"form": form})

def editAuto(request, id):
    auto= Auto.objects.get(id=id)
    if request.method=="POST":
        form= AutoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca= info["marca"]
            modelo= info["modelo"]
            anio= info["anio"]
            airbag= info["airbag"]
            auto.marca= marca
            auto.modelo= modelo
            auto.anio= anio
            auto.airbag= airbag
            auto.save()
            autos= Auto.objects.all()
            return render(request, "autos.html", {"autos": autos, "mensaje": "Auto Editado"})
    else:
        form= AutoForm(initial={"marca": auto.marca, "modelo": auto.modelo, "anio": auto.anio, "airbag": auto.airbag})
        return render(request, "editauto.html", {"form": form, "auto": auto})

def delAuto(request, id):
    auto= Auto.objects.get(id=id)
    auto.delete()
    autos= Auto.objects.all()
    return render(request, "autos.html", {"autos": autos, "mensaje": "Auto Eliminado"})

def searchAuto(request):
    return render(request, "searchautos.html")

def foundAuto(request):
    marca= request.GET["marca"]
    if marca!="":
        autos= Auto.objects.filter(marca__icontains=marca)
        return render(request, "foundautos.html", {"autos": autos})
    else:
        return render(request, "searchautos.html", {"mensaje": "Campo vacío."} )

#          #          #          #          #          #          #          #          
#          PERROS
#          #          #          #          #          #          #          #          

def listaPerros(request):
    perros= Perro.objects.all()
    return render(request, "perros.html", {"perros": perros})

def addPerro(request):
    if request.method=="POST":
        form= PerroForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            perro= Perro(nombre=info["nombre"], raza=info["raza"], genero=info["genero"], edad=info["edad"])
            perro.save()
            perros= Perro.objects.all()
            return render(request, "perros.html", {"perros": perros})
        else:
            return render(request, "formperros.html", {"form": form, "mensaje": "Algo malió sal."})
    else:
        form= PerroForm()
        return render(request, "formperros.html", {"form": form})

def editPerro(request, id):
    perro= Perro.objects.get(id=id)
    if request.method=="POST":
        form= PerroForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            raza= info["raza"]
            genero= info["genero"]
            edad= info["edad"]
            perro.nombre= nombre
            perro.raza= raza
            perro.genero= genero
            perro.edad= edad
            perro.save()
            perros= Perro.objects.all()
            return render(request, "perros.html", {"perros": perros, "mensaje": "Perro Editado"})
    else:
        form= PerroForm(initial={"nombre": perro.nombre, "raza": perro.raza, "genero": perro.genero, "edad": perro.edad})
        return render(request, "editperro.html", {"form": form, "perro": perro})

def delPerro(request, id):
    perro= Perro.objects.get(id=id)
    perro.delete()
    perros= Perro.objects.all()
    return render(request, "perros.html", {"perros": perros, "mensaje": "Perro Eliminado"})

def searchPerro(request):
    return render(request, "searchperros.html")

def foundPerro(request):
    raza= request.GET["raza"]
    if raza!="":
        perros= Perro.objects.filter(raza__icontains=raza)
        return render(request, "foundperros.html", {"perros": perros})
    else:
        return render(request, "searchperros.html", {"mensaje": "Campo vacío."} )

#          #          #          #          #          #          #          #          
#          EQUIPOS
#          #          #          #          #          #          #          #          

def listaEquipos(request):
    equipos= Equipo.objects.all()
    return render(request, "equipos.html", {"equipos": equipos})

def addEquipo(request):
    if request.method=="POST":
        form= EquipoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            equipo= Equipo(pais=info["pais"], continente=info["continente"], sigueJugando=info["sigueJugando"])
            equipo.save()
            equipos= Equipo.objects.all()
            return render(request, "equipos.html", {"equipos": equipos})
        else:
            return render(request, "formequipos.html", {"form": form, "mensaje": "Algo malió sal."})
    else:
        form= EquipoForm()
        return render(request, "formequipos.html", {"form": form})

def editEquipo(request, id):
    equipo= Equipo.objects.get(id=id)
    if request.method=="POST":
        form= EquipoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            pais= info["pais"]
            continente= info["continente"]
            sigueJugando= info["sigueJugando"]
            equipo.pais= pais
            equipo.continente= continente
            equipo.sigueJugando= sigueJugando
            equipo.save()
            equipos= Equipo.objects.all()
            return render(request, "equipos.html", {"equipos": equipos, "mensaje": "Equipo Editado"})
    else:
        form= EquipoForm(initial={"pais": equipo.pais, "continente": equipo.continente, "sigueJugando": equipo.sigueJugando})
        return render(request, "editequipo.html", {"form": form, "equipo": equipo})

def delEquipo(request, id):
    equipo= Equipo.objects.get(id=id)
    equipo.delete()
    equipos= Equipo.objects.all()
    return render(request, "equipos.html", {"equipos": equipos, "mensaje": "Equipo Eliminado"})

def searchEquipo(request):
    return render(request, "searchequipos.html")

def foundEquipo(request):
    continente= request.GET["continente"]
    if continente!="":
        equipos= Equipo.objects.filter(continente=continente)
        return render(request, "foundequipos.html", {"equipos": equipos})
    else:
        return render(request, "searchequipos.html", {"mensaje": "Campo vacío."})