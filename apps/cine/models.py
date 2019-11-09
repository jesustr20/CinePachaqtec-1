from django.db import models

# Create your models here.
class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    direccion = models.CharField(max_length=220, blank=False, null=False)
    sevicio = models.TextField(blank=False, null=False)
    distrito = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name= 'Pelicula'
        verbose_name_plural= 'Peliculas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre     