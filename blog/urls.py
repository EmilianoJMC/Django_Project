from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('pages/', PostListView.as_view(), name='pages'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('pages/novo/', PostCreateView.as_view(), name='post_create'),
    path('pages/<int:pk>/editar/', PostUpdateView.as_view(), name='post_edit'),
    path('pages/<int:pk>/excluir/', PostDeleteView.as_view(), name='post_delete'),
] 