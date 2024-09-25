import os
from django.shortcuts import render,redirect
from .models import Ingresos,Usuarios
from django.http import JsonResponse,HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string
import io
import openpyxl
from openpyxl.styles import Font

# Create your views here.
def home(request):
    ingresos = Ingresos.objects.all()
    usuarios = Usuarios.objects.all()
    ingresos_invertidos = []
    for i in ingresos[::-1]:
        ingresos_invertidos.append(i)
    return render(request,"ingresos/ingresos.html",{"ingresos":ingresos_invertidos,"usuarios":usuarios})

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


def detalleIngreso(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    return render(request,"ingresos/detalleIngresos.html",{"ingreso":ingreso})

def editarIngreso(request,nIngreso):
    pago = request.POST['tipo_pago']
    valor =request.POST['valorIngreso']
    concepto =request.POST['concepto']   
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    ingreso.tipo_pago = pago
    ingreso.valorIngreso = valor
    ingreso.concepto = concepto
    ingreso.save()
    return redirect('/')


def verificar_cedula(request):
    cedula = request.GET.get('cedula', None)
    if cedula:
        try:
            usuario = Usuarios.objects.get(cedula=cedula)
            data = {
                'usuario': {
                    'nombre_completo': usuario.nombre_completo,
                    'direccion': usuario.direccion,
                }
            }
        except Usuarios.DoesNotExist:
            data = {'usuario': None}
    else:
        data = {'usuario': None}
    
    return JsonResponse(data)

def detallePDF(request,nIngreso):
    ingreso = Ingresos.objects.get(nIngreso=nIngreso)
    return render(request,"ingresos/ticketIngresos.html",{"ingreso":ingreso})

def export_to_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Personas'
        
    sheet.append(['nIngreso', 'Nombre', 'Cedula','Direccion', 'Metodo de Pago', 'Valor','Concepto', 'Ciudad', 'Fecha'])
    for cell in sheet[1]:
        cell.font = Font(bold=True) 
    
    ingresos = Ingresos.objects.all()
    
    for ingreso in ingresos:
        if ingreso.fecha:
            fecha = ingreso.fecha.replace(tzinfo=None)
        else:
            fecha= None
        sheet.append([ingreso.nIngreso, ingreso.usuario.nombre_completo, ingreso.usuario.cedula,ingreso.usuario.direccion, ingreso.tipo_pago, ingreso.valorIngreso,ingreso.concepto, ingreso.ciudad, fecha])
         
    for column in sheet.columns:
        max_length = max(len(str(cell.value)) for cell in column if cell.value)  # Encuentra el texto más largo
        adjusted_width = max_length + 2  # Añadir un pequeño margen
        sheet.column_dimensions[column[0].column_letter].width = adjusted_width
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ingresos.xlsx"'     

    workbook.save(response)

    return response