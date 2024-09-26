from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
           
    def __str__(self):
        texto = f"{self.cedula:} {self.nombre_completo}"
        return texto

class Vacunadores(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    municipio = models.CharField(max_length=255)
           
    def __str__(self):
        texto = f"{self.cedula:} {self.nombre_completo}"
        return texto


class Ingresos(models.Model):
    nIngreso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100,default='San Juan Nepomuceno',editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    valorIngreso = models.IntegerField(default=0,blank=True,null=True)
    concepto = models.CharField(max_length=200)
    
    def __str__(self):
        texto = f"{self.nIngreso} {self.valorIngreso} {self.concepto}"
        return texto
    
class Egresos(models.Model):
    nEngreso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100,default='San Juan Nepomuceno',editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    valorIngreso = models.IntegerField(default=0,blank=True,null=True)
    concepto = models.CharField(max_length=200)
    
    def __str__(self):
        texto = f"{self.nIngreso} {self.valorIngreso} {self.concepto}"
        return texto