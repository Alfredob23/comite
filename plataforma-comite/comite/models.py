from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
           
    def __str__(self):
        texto = f"{self.cedula:} {self.nombre_completo}"
        return texto

class Biologicos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    valorUnidad = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} Valor: {self.valorUnidad}"


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
    infoAftosa = models.ForeignKey(Biologicos, on_delete=models.CASCADE,null=True,related_name='info_aftosa')
    infoCepa = models.ForeignKey(Biologicos, on_delete=models.CASCADE,null=True,related_name='info_cepa')
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,null=True)
    cantidad_aftosa = models.IntegerField(default=0)
    cantidad_cepa19 = models.IntegerField(default=0)
    cantidad_total = models.JSONField()
    biologico = models.JSONField()
    lote = models.JSONField()
    laboratorio = models.JSONField()
    valor_total = models.BigIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    

    def save(self, *args, **kwargs):     
        
        #Obtengo la informacion de los Biologicos para posteriormente hacer un calculo del valor total
        self.infoAftosa = Biologicos.objects.get(nombre='Aftosa')
        self.infoCepa = Biologicos.objects.get(nombre='Cepa19')
        if self.infoAftosa:
            self.valor_total = int(self.cantidad_aftosa) * int(self.infoAftosa.valorUnidad)
        
        # recorro el campo Biologico y Cantidad total, para que en el momento que se realice un cambio 
        # en los valores de cantidad total, se actualice la cantidad de biologicos y por ende el valor total    
        self.cantidad_aftosa = 0
        self.cantidad_cepa19 = 0
        for b,c in zip(self.biologico,self.cantidad_total):
            if b=='Aftosa':
                self.cantidad_aftosa +=c
            elif b == 'Cepa19':
                self.cantidad_cepa19 +=c            

        super().save(*args, **kwargs)
         
    def __str__(self):
        biologico1_nombre = self.biologico if self.biologico else "No asignado"
        texto = f"Factura No: {self.nFactura} Biologico1: {biologico1_nombre}"
        return texto
    
    
