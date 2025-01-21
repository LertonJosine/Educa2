from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UsuarioCustomizado(AbstractUser):
    nome_do_pai = models.CharField(max_length=200, default='')
    def get_absolute_url(self):
        return reverse("login")
    