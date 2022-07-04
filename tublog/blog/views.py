from xml.etree.ElementTree import Comment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

#def home(request):
    #return render(request, 'home.html', {}) 

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class AboutView(ListView):
    model = Post
    template_name = 'acerca_de_mi.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalles_articulo.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crear_articulo.html'
    #fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'crear_comentario.html'
    #fields = '__all__'

    def form_valid( self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
   model = Category
   template_name = 'crear_categoria.html'
   fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'actualizar_articulo.html'
    #fields = ['titulo', 'etiqueta_titulo', 'autor', 'cuerpo']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'borrar_articulo.html'
    success_url = reverse_lazy('home')

