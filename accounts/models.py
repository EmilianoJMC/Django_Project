from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia = models.TextField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
