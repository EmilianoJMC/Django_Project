from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    conteudo = RichTextField()
    imagem = models.ImageField(upload_to='posts/')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
