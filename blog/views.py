from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages.html'
    context_object_name = 'posts'
    ordering = ['-data_criacao']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'conteudo', 'imagem']
    success_url = reverse_lazy('pages')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'conteudo', 'imagem']
    success_url = reverse_lazy('pages')

    def test_func(self):
        # Permite editar apenas se o usuário for staff ou superuser
        return self.request.user.is_staff or self.request.user.is_superuser

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('pages')

    def test_func(self):
        # Permite excluir apenas se o usuário for staff ou superuser
        return self.request.user.is_staff or self.request.user.is_superuser
