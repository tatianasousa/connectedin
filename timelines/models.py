from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    texto = models.TextField(max_length=1000, null=False)
    usuario = models.ForeignKey(User, related_name='perfil', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario