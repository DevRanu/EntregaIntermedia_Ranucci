from django.urls import path
from .views import *


urlpatterns = [
    path('categorias/', categorias, name="categorias"),
    path("autos/", listaAutos, name="autos"),
    path("addAuto/", addAuto, name="addAuto"),
    path("editAuto/<id>", editAuto, name="editAuto"),
    path("delAuto/<id>", delAuto, name="delAuto"),
    path("searchAuto/", searchAuto, name="searchAuto"),
    path("foundAuto/", foundAuto, name="foundAuto"),
    
    path("perros/", listaPerros, name="perros"),
    path("addPerro/", addPerro, name="addPerro"),
    path("editPerro/<id>", editPerro, name="editPerro"),
    path("delPerro/<id>", delPerro, name="delPerro"),
    path("searchPerro/", searchPerro, name="searchPerro"),
    path("foundPerro/", foundPerro, name="foundPerro"),

    path("equipos/", listaEquipos, name="equipos"),
    path("addEquipo/", addEquipo, name="addEquipo"),
    path("editEquipo/<id>", editEquipo, name="editEquipo"),
    path("delEquipo/<id>", delEquipo, name="delEquipo"),
    path("searchEquipo/", searchEquipo, name="searchEquipo"),
    path("foundEquipo/", foundEquipo, name="foundEquipo"),
]