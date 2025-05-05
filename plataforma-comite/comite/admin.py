from django.contrib import admin
from .models import Ingresos,Usuarios,Egresos,Biologicos,Facturar,Mensajes
# Register your models here.

admin.site.register(Ingresos)
admin.site.register(Usuarios)
admin.site.register(Egresos)
admin.site.register(Biologicos)
admin.site.register(Facturar)
admin.site.register(Mensajes)
