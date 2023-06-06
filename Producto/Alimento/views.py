from django.shortcuts import render, redirect
from .models import Aliment
# Create your views here.

def home(request):
    aliment=Aliment.objects.all()
    return render(request,"gestionproducto.html", {"alimento": aliment})


def registrarProducto(request):
    codigo=request.POST["txtCodigo"]
    nombre=request.POST["txtNombre"]
    catador=request.POST["Catador"]
    
    aliment= Aliment.objects.create(
        codigo=codigo, nombre=nombre, catador=catador)
    
    return redirect('/')

def edicionProducto(request,codigo):
    aliment = Aliment.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"aliment":aliment})

def eliminacionProducto(request, codigo):
    aliment=Aliment.objects.get(codigo=codigo)
    aliment.delate()
    return redirect('/')