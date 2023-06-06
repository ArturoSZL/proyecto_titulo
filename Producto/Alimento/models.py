from django.db import models

# Create your models here.

class Aliment(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    catador=models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto="{0} ({1})"
