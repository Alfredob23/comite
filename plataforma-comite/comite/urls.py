from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarIngreso/',views.registrarIngreso),
    path('edicionIngreso/<nIngreso>',views.edicionIngreso),
    path('eliminacionIngreso/<nIngreso>',views.eliminacionIngreso),
    path('editarIngreso/<int:nIngreso>/',views.editarIngreso),
    path('detalleIngreso/<int:nIngreso>/',views.detalleIngreso),
    path('verificar-cedula/', views.verificar_cedula, name='verificar_cedula'),
    path('detallePDF/<int:nIngreso>', views.detallePDF,),
    path('descargarExcel/',views.export_to_excel,name='exportar a excel'),
    path('egresos/',views.egresos),
    path('registrarEgreso/',views.registrarEgreso),
    path('egresos/detalleEgreso/<int:nEgreso>/',views.detalleEgreso),
    path('egresos/eliminacionEgreso/<nEgreso>',views.eliminacionEgreso),
    path('egresos/edicionEgreso/<nEgreso>',views.edicionEgreso),
    path('egresos/editarEgreso/<int:nEgreso>/',views.editarEgreso),
    path('egresos/imprimirEgreso/<int:nEgreso>', views.imprimirEgreso)

]