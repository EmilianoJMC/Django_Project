from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView, RegistroView,
    PerfilDetailView, PerfilUpdateView, UserUpdateView, CustomPasswordChangeView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistroView.as_view(), name='register'),
    path('perfil/', PerfilDetailView.as_view(), name='perfil'),
    path('perfil/editar/', PerfilUpdateView.as_view(), name='editar_perfil'),
    path('usuario/editar/', UserUpdateView.as_view(), name='editar_usuario'),
    path('senha/', CustomPasswordChangeView.as_view(), name='password_change'),
] 