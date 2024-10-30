from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
           
    def __str__(self):
        texto = f"{self.cedula:} {self.nombre_completo}"
        return texto

class Vacunas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor_unitario = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ingresos(models.Model):
    nIngreso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,null=True)
    tipo_pago = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100,default='San Juan Nepomuceno',editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    valorIngreso = models.IntegerField(default=0,blank=True,null=True)
    concepto = models.CharField(max_length=200)
    
    def __str__(self):
        texto = f"{self.nIngreso} {self.valorIngreso} {self.concepto}"
        return texto
    
class Egresos(models.Model):
    nEgreso = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=20)
    valorEgreso = models.IntegerField(default=0,blank=True,null=True)
    concepto = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100,default='San Juan Nepomuceno',editable=False)
    recibe = models.CharField(max_length=100, null=False)
    aprobado = models.CharField(max_length=100,default='Jorge Arzuaga',editable=False)
    revisado = models.CharField(max_length=100,default='Jorge Arzuaga',null=False)
    contabilizado = models.CharField(max_length=100,default='Eduard Posso',editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    

    
    def __str__(self):
        texto = f"{self.nEgreso} {self.valorEgreso} {self.concepto}"
        return texto
    
    
class Facturar(models.Model):
    nFactura = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,null=True)
    vacunas = models.ForeignKey(Vacunas, on_delete=models.CASCADE,null=True)
    cantidad_vacunas = models.IntegerField(default=0)
    lote = models.IntegerField(default=0)
    laboratio = models.CharField(max_length=100)
    valor_total = models.IntegerField(default=0,editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.valor_total = self.cantidad_vacunas* self.vacunas.valor_unitario
        super().save(*args, **kwargs) 
         
    def __str__(self):
        texto = f"{self.nFactura} {self.vacunas.nombre} {self.cantidad_vacunas}"
        return texto