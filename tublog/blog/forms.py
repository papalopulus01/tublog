from django import forms 
from .models import Post, Category, Comment 

choices = Category.objects.all().values_list('nombre', 'nombre')
choice_list = [] 

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('titulo', 'etiqueta_titulo', 'autor', 'categoria', 'cuerpo', 'vista', 'imagen_de_cabecera')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el título de tu publicación'}),
            'etiqueta_titulo': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Escribe la etiqueta de tu publicación'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Escribe tu publicación'}),
            'vista': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Escribe una vista previa para la página principal'}),
        
        
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('titulo', 'etiqueta_titulo', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el título de tu publicación'}),
            'etiqueta_titulo': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Escribe la etiqueta de tu publicación'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Escribe tu publicación'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nombre', 'cuerpo')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Escribe tu comentario'}),
        }