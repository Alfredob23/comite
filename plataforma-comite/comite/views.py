from django.shortcuts import render,redirect
from .models import Ingresos,Usuarios

# Create your views here.
def home(request):
    ingresos = Ingresos.objects.all()
    return render(request,"ingresos/ingresos.html",{"ingresos":ingresos})

def registrarIngreso(request):
    cedula = request.POST['cedula']
    nombre_completo = request.POST['nombre_completo']
    direccion = request.POST['direccion']
    tipo_pago = request.POST['tipo_pago']
    valorIngreso = request.POST['valorIngreso']
    concepto = request.POST['concepto']
    if cedula and nombre_completo and direccion:
        usuario, created = Usuarios.objects.get_or_create(cedula=cedula, defaults={'nombre_completo': nombre_completo,'direccion': direccion})
                # Si el usuario fue creado correctamente, creamos el ingreso
        if usuario:
            Ingresos.objects.create(usuario=usuario, tipo_pago=tipo_pago,valorIngreso=valorIngreso,concepto=concepto)
            return redirect('/')
    else:
        return render(request, '/', {'error': 'Todos los campos son requeridos.'})
    return render(request, '/')



def eliminacionIngreso(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    ingreso.delete()
    return redirect('/')

def edicionIngreso(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    return render(request,"ingresos/edicionIngresos.html",{"ingreso":ingreso})

def editarIngreso(request,nIngreso):
    pago = request.POST['mPago']
    valor =request.POST['numValor']
    concepto =request.POST['concepto']   
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    ingreso.tipo_pago = pago
    ingreso.valorIngreso = valor
    ingreso.concepto = concepto
    ingreso.save()
    return redirect('/')

def prueba(request):
    if request.method == 'POST':
            # Obtener los datos del formulario
            cedula = request.POST.get('cedula')
            nombre_completo = request.POST.get('nombre_completo')
            direccion = request.POST.get('direccion')
            tipo_pago = request.POST.get('tipo_pago')
            valorIngreso = request.POST.get('valorIngreso')
            concepto = request.POST.get('concepto')

            # Crear el nuevo usuario
            if cedula and nombre_completo and direccion:
                usuario, created = Usuarios.objects.get_or_create(cedula=cedula, defaults={'nombre_completo': nombre_completo,'direccion': direccion})
                # Si el usuario fue creado correctamente, creamos el ingreso
                if usuario:
                    Ingresos.objects.create(usuario=usuario, tipo_pago=tipo_pago,valorIngreso=valorIngreso,concepto=concepto)
                    return redirect('/')
            else:
                return render(request, 'prueba.html', {'error': 'Todos los campos son requeridos.'})
    return render(request, 'prueba.html')
        
