from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    
    def _str_(self):
        return f"{self.nombre}-{self.apellido}"