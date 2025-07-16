"""
Views de autenticação, registro, perfil e alteração de senha do usuário.
Utiliza CBVs, mixins e integração com sistema de mensagens do Django.
"""
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Perfil
from .forms import RegistroForm, PerfilForm, UserForm
from . import signals
from django.shortcuts import get_object_or_404

class CustomLoginView(LoginView):
    """View de login de usuário."""
    template_name = 'registration/login.html'
    def form_valid(self, form):
        messages.success(self.request, 'Login realizado com sucesso!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    """View de logout de usuário."""
    next_page = reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        messages.info(request, 'Logout realizado. Até logo!')
        return self.post(request, *args, **kwargs)

class RegistroView(CreateView):
    """View de registro de novo usuário."""
    model = User
    form_class = RegistroForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cadastro realizado com sucesso! Faça login.')
        return response

class PerfilDetailView(LoginRequiredMixin, DetailView):
    """Exibe o perfil do usuário logado ou de outro usuário."""
    model = Perfil
    template_name = 'accounts/perfil.html'
    context_object_name = 'perfil'
    def get_object(self):
        username = self.kwargs.get('username')
        if username:
            return Perfil.objects.get(user__username=username)
        perfil, created = Perfil.objects.get_or_create(user=self.request.user)
        return perfil

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    """Permite editar o perfil do usuário logado."""
    model = Perfil
    form_class = PerfilForm
    template_name = 'accounts/editar_perfil.html'
    success_url = reverse_lazy('perfil')
    def get_object(self):
        obj = Perfil.objects.get(user=self.request.user)
        return obj
    def form_valid(self, form):
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Permite editar dados básicos do usuário logado."""
    model = User
    form_class = UserForm
    template_name = 'accounts/editar_usuario.html'
    success_url = reverse_lazy('perfil')
    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        messages.success(self.request, 'Dados de usuário atualizados!')
        return super().form_valid(form)

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Permite alterar a senha do usuário logado."""
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('perfil')
    def form_valid(self, form):
        messages.success(self.request, 'Senha alterada com sucesso!')
        return super().form_valid(form)
