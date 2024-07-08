from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=30)             
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    multiplicador = models.IntegerField(choices=((1,'+'), (-1, '-')),default=1)
        
    def __str__(self):
        return self.name

class Operaciones(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True,default='OPT')
    fecha_creacion = models.DateField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True) 
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null = True)    
    fecha_pago = models.DateField(null=True, blank=True)
    monto =  models.PositiveIntegerField(default=0)    
    #id_boleta = models.IntegerField(null=False,default=0)
    #id_deuda =  models.CharField(max_length=250)     

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:  # Si el objeto aún no tiene ID, se guarda primero
            super().save(*args, **kwargs)
        if self.name=='OPT':  # Si el campo 'name' está vacío
            self.name = f"OPT{str(self.id)}"  # Asigna el valor del 'id' al 'name'
            super().save(*args, **kwargs)  # Guarda el objeto de nuevo con el 'name' actualizado
        else:
            super().save(*args, **kwargs) # Guarda el objeto normalmente si 'name' ya tiene valor

@receiver(post_save, sender=Operaciones)
def update_name_with_id(sender, instance, created, **kwargs):
    if created and instance.name =='OPT':
        instance.name = f"OPT{instance.id}"
        instance.save()