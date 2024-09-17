from django.shortcuts import render,redirect
from .models import Ingresos

# Create your views here.
def home(request):
    ingresos = Ingresos.objects.all()
    return render(request,"ingresos/ingresos.html",{"ingresos":ingresos})

def registrarIngreso(request):
    pago = request.POST['opciones']
    valor =request.POST['numValor']
    concepto =request.POST['opciones1']   
    ingreso = Ingresos.objects.create(tipo_pago =pago,valorIngreso=valor,concepto =concepto)
    return redirect('/')

def eliminacionIngreso(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    ingreso.delete()
    return redirect('/')

def edicionIngreso(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    return render(request,"ingresos/edicionIngresos.html",{"ingreso":ingreso})

def editarIngreso(request,nIngreso):
    pago = request.POST['opciones']
    valor =request.POST['numValor']
    concepto =request.POST['opciones1']   
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    ingreso.tipo_pago = pago
    ingreso.valorIngreso = valor
    ingreso.concepto = concepto
    ingreso.save()
    return redirect('/')