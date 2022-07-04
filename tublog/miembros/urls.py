from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='register'),
    path('editar_perfil/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordChangeView.as_view(template_name='registration/cambiar-password.html')),  
    path('password_cambiado_con_exito', views.password_success, name='password_cambiado_con_exito'),
] 
