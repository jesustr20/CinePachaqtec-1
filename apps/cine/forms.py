from django import forms
from .models import Local, Pelicula, Sala, Funcion, Actor

#JESUS
class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = {'nombre', 'direccion', 'tiposervicio', 'precio','distrito','imagen'}
        labels = {
            'nombre': 'Nombre del local',
            'direccion': 'Direccion del local',
            'tiposervicio': 'Tipo de servicio del local',
            'precio': 'Precio pelicula del local',
            'distrito': 'Distrito del local',
            'imagen': 'Imagen del local'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del Local',
                    'id': 'nombre'
                    }
                ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la direccion del Local',
                    'id': 'direccion'
                    }
                ),
            'tiposervicio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el tiposervicio del Local',
                    'id': 'tiposervicio'
                    }
                ),
            'distrito': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'distrito'
                    }
                ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                    }
                )
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['id_local', 'trailer', 'titulo', 'genero', 'duracion',
            'categoria', 'imagen', 'sinopsis', 'director', 'idioma']
        labels = {
            'id_local': 'Local',
            'trailer': 'Trailer',
            'titulo': 'Titulo',
            'genero': 'Genero',
            'duracion': 'Duracion',
            'categoria': 'Categoria',
            'imagen': 'Imagen',
            'sinopsis': 'Sinopsis',
            'director': 'Director',
            'idioma': 'Idioma'
        }
        widgets = {
            'id_local': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre de la pelicula',
                    'id': 'id_local'
                    }
                ),
            'trailer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Trailer de la pelicula',
                    'id': 'trailer'
                    }
                ),
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Titulo de la pelicula',
                    'id': 'titulo'
                    }
                ),
            'genero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Genero de la pelicula',
                    'id': 'genero'
                    }
                ),
            'duracion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'duracion'
                    }
                ),
            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'categoria'
                    }
                ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                    }
                ),
            'sinopsis': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'sinopsis'
                    }
                ),
            'director': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'director'
                    }
                ),
            'idioma': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'idioma'
                    }
                )
        }

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre']
        labels = {
            'nombre': 'Local de la pelicula'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del local',
                    'id': 'nombre'
                    }
                )
        }

#MAGALY
class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = {'hora_funcion','id_local','id_pelicula','id_sala'}

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = {'id_pelicula','nombre','imagen'}
        labels = {
            'id_pelicula' : 'Seleccionar Pelicula',
            'nombre': 'Nombre del actor',
            'imagen': 'Seleccionar imagen'
        }