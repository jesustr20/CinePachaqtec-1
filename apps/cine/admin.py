from django.contrib import admin
from .models import Local, Pelicula, Sala, Actor, Funcion, Venta, Usuario

# Register your models here.
admin.site.register(Local)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Actor)
admin.site.register(Funcion)