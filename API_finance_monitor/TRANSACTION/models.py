from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=30)             
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    #multiplicador = models.IntegerField(choices=((1,'+'), (-1, '-')),default=1)
        
    def __str__(self):
        return self.name

class Operaciones(models.Model):
    name = models.CharField(max_length=100)
    fecha_creacion = models.DateField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True) 
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null = True)    
    fecha_pago = models.DateField(null=True, blank=True)
    monto =  models.PositiveIntegerField(default=0)    
    #id_boleta = models.IntegerField(null=False,default=0)
    #id_deuda =  models.CharField(max_length=250)     

    def __str__(self):        
        return self.name

