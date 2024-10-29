from django.contrib import admin
from .models import Ingresos,Usuarios,Egresos,Vacunas,Facturar
# Register your models here.

admin.site.register(Ingresos)
admin.site.register(Usuarios)
admin.site.register(Egresos)
admin.site.register(Vacunas)
admin.site.register(Facturar)
