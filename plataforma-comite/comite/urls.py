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
    path('descargarExcel/',views.export_to_excel,name='exportar a excel')
    

]