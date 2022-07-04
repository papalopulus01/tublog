from django.urls import path
from .views import HomeView, AboutView, ArticleDetailView, AddPostView, AddCommentView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('acerca_de_mi', AboutView.as_view(), name='acerca_de_mi'),
    path('articulo/<int:pk>', ArticleDetailView.as_view(), name='detalles_articulo'),
    path('crear_articulo/', AddPostView.as_view(), name='crear_articulo'),
    path('crear_categoria/', AddCategoryView.as_view(), name='crear_categoria'),
    path('articulo/editar/<int:pk>', UpdatePostView.as_view(), name='actualizar_articulo'),
    path('articulo/<int:pk>/eliminar', DeletePostView.as_view(), name='borrar_articulo'),
    path('articulo/<int:pk>/comentario', AddCommentView.as_view(), name='crear_comentario'),

]
