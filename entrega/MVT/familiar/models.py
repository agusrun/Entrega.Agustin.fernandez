from django.db import models
class familia (models.Model):
    nombre=models.CharField(max_length=50)
    dni=models.IntegerField()
    nacimiento=models.DateField()
    
