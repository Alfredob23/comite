from django.db import models
from django.db.models import Sum

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
    facturas = models.ForeignKey("Facturar", on_delete=models.CASCADE,null=True)
    tipo_pago = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100,default='San Juan Nepomuceno',editable=False)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    valorIngreso = models.IntegerField(default=0,blank=True,null=True)
    concepto = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) 
        
        if self.facturas:
            factura = Facturar.objects.get(nFactura=self.facturas.nFactura)
            n_factura_especifica = factura.nFactura
            factura.valor_pagado = Ingresos.objects.filter(facturas__nFactura=n_factura_especifica).aggregate(total_pagado=Sum('valorIngreso'))['total_pagado']  
            factura.save()
        
    def delete(self, *args, **kwargs):
        factura = self.facturas
        super().delete(*args, **kwargs)
        if factura:
            factura.valor_pagado = Ingresos.objects.filter(facturas=factura).aggregate(Sum('valorIngreso'))['valorIngreso__sum'] or 0
            factura.valor_pendiente = factura.valor_total - factura.valor_pagado
            factura.save()
            
    def __str__(self):
        biologico1_nombre = self.biologico if self.biologico else "No asignado"
        texto = f"Factura No: {self.nFactura} Biologico1: {biologico1_nombre}"
        return texto
    
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
    nFactura= models.CharField(max_length=10, primary_key=True, editable=False)
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
    valor_pagado = models.IntegerField(default=0)
    valor_pendiente = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True,editable=False)
    estatus = models.CharField(max_length=20,default='PENDIENTE', )
       
    def save(self, *args, **kwargs):   
        #Obtengo la informacion de los Biologicos para posteriormente hacer un calculo del valor total
        self.infoCepa = Biologicos.objects.get(nombre='Cepa19')
        self.infoAftosa = Biologicos.objects.get(nombre='Aftosa')
        
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
        #En esta parte valido le asigno valor a 'valor_pediente' y tambienanalizo si  el valor pagado es superior o inferior al valor total
        #para de esta manera asignarle un estatus a la factura      

        self.valor_pendiente = int(self.valor_total) - int(self.valor_pagado)
        if int(self.valor_pendiente) <= 0:
            self.valor_pendiente = 0
        if int(self.valor_pagado)>= self.valor_total:
            self.estatus = 'PAGADO'
        elif int(self.valor_pagado) > 0:
            self.estatus = 'ABONADO'
        else:
            self.estatus = 'PENDIENTE'
        #  En esta parte, se le da formato al ID y se verifica cual es el ultimo valor
        # y se incrementa ejemplo FA1,FA2,FA3             
        if not self.nFactura:  # Si el ID no está definido
                    ultimo = Facturar.objects.order_by('-nFactura').first()  # Obtener el último registro
                    if ultimo:
                        # Extraer la parte numérica del ID (suponiendo formato "FA1", "FA2", ...)
                        ultimo_id_num = int(ultimo.nFactura[2:])
                        nuevo_id = f"FA{ultimo_id_num + 1}"
                    else:
                        nuevo_id = "FA1"  # Primer registro
                    self.nFactura = nuevo_id

        super().save(*args, **kwargs)
         
    def __str__(self):
        biologico1_nombre = self.biologico if self.biologico else "No asignado"
        texto = f"Factura No: {self.nFactura} Biologico1: {biologico1_nombre}"
        return texto
    
    
class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        texto = f"{self.nombre} {self.correo}"
        return texto