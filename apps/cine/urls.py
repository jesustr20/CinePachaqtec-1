from django.urls import path
from .views import Local_listar, Pelicula_listar
from .views import ListarFunciones, CrearFuncion
from .views import CrearActor, ListarActores, EditarActor, EliminarActor
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #JESUS
    #Locales
    path('local_listar/', login_required(Local_listar.as_view()), name='local_listar'),
    
    #Peliculas
    path('pelicula_listar/', login_required(Pelicula_listar.as_view()), name='pelicula_listar'),

    #MAGALY
    #Actores
    path('listar_actores/', login_required(ListarActores.as_view()), name ='listar_actores'),
    path('crear_actor/', CrearActor.as_view(), name = 'crear_actor'),
    path('editar_actor/<int:pk>', EditarActor.as_view(), name='editar_actor' ),
    path('eliminar_actor/<int:pk>', EliminarActor.as_view(), name='eliminar_actor' ),

    #FUNCIONES
    path('listar_funciones/', login_required(ListarFunciones.as_view()), name='listar_funciones'),
    path('crear_funcion/', CrearFuncion.as_view(), name='crear_funcion'),  

]