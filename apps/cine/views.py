from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Local, Pelicula, Actor, Funcion
from .forms import LocalForm, PeliculaForm, ActorForm, FuncionForm

# Create your views here. -> JESUS TUESTA
class Home(TemplateView):
    template_name = 'cine/index.html'

    def get_context_data(self, *args, **kwargs):
        locales = Local.objects.all()
        context = super(Home,self).get_context_data(*args, **kwargs)
        context['locales'] = locales
        return context

class Local_listar(ListView):
    model = Local
    template_name = 'cine/local/local_listar.html'
    queryset = Local.objects.all()
    context_object_name = 'locales'

class Pelicula_listar(ListView):
    model = Pelicula
    template_name = 'cine/local/pelicula_listar.html'
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'


#MAGALY

class CrearFuncion(CreateView):
    model = Funcion
    form_class = FuncionForm
    template_name = 'cine/funcion/crear_funcion.html'
    success_url = reverse_lazy('cine:listar_funciones')

class ListarFunciones(ListView):
    model = Funcion
    template_name = 'cine/funcion/listar_funcion.html'
    queryset = Funcion.objects.all()
    context_object_name='funciones'

class CrearActor(CreateView):
    model = Actor
    form_class = ActorForm
    template_name ='cine/actor/crear_actor.html'
    success_url = reverse_lazy ('cine:listar_actores')

class ListarActores(ListView):
    model = Actor
    template_name = 'cine/actor/listar_actor.html'
    queryset = Actor.objects.all()
    context_object_name = 'actores'


class EditarActor(UpdateView):
    model = Actor
    form_class=ActorForm
    template_name='cine/actor/editar_actor.html'
    success_url = reverse_lazy('cine:listar_actores')

class EliminarActor(DeleteView):
    model = Actor
    form_class=ActorForm
    template_name='cine/actor/eliminar_actor.html'
    success_url = reverse_lazy('cine:listar_actores')
    
    def get_context_data(self,*args,**kwards):
        actor = Actor.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarActor,self).get_context_data(*args,**kwards)
        context['actor'] = actor