from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 
from ckeditor.fields import RichTextField

class Category(models.Model):
   nombre = models.CharField(max_length=255)

   def __str__(self):
     return self.nombre

   def get_absolute_url(self):
     return reverse('home')

class Profile(models.Model):
   usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
   biografia = models.TextField()
   foto_perfil = models.ImageField(null=True, blank=True, upload_to="imagenes/perfiles/")
   direccion_paginaweb = models.CharField(max_length=255, null=True, blank=True)
   direccion_instagram = models.CharField(max_length=255, null=True, blank=True)
   direccion_twitter = models.CharField(max_length=255, null=True, blank=True)
   direccion_tikTok = models.CharField(max_length=255, null=True, blank=True)

   def __str__(self):
      return str(self.usuario)

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    imagen_de_cabecera = models.ImageField(null = True, blank=True, upload_to="imagenes/")
    etiqueta_titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    categoria = models.CharField(max_length=255, default="Sin categoría")
    vista = models.CharField(max_length=255)

    def __str__(self):
     return self.titulo + ' | ' + str(self.autor) 

    def get_absolute_url(self):
     return reverse('home')

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
  nombre = models.CharField(max_length=255)
  cuerpo = models.TextField()
  fecha_agregado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.post.titulo, self.nombre) 

  

