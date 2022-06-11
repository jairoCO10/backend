from django.db import models
# Create your models here.

# add this
class datos_empresas(models.Model):
  nombre_empresa = models.CharField(max_length=120)
  direccion = models.CharField(max_length=150)
  nit = models.IntegerField()
  telefono = models.CharField(max_length=20)
      
  def __str__(self):
    return self.title