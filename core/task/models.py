from django.db import models

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)

    def _str_(self):
        return f'{self.titulo} - {self.descripcion}'