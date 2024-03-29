from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Autor', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=60, blank=True, null=True)
    seguidores = models.ManyToManyField("Pessoa", verbose_name='Seguidores')

    def __str__(self):
        return self.usuario.username


class Publicacao(models.Model):
    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Pessoa, verbose_name='Autor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto

    def get_absolute_url(self):
        return reverse("detalhes", kwargs={"public_id": self.pk})

    def __str__(self):
        return "Post feito por:" + " " + self.autor.username


class Comentario(models.Model):
    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Pessoa, related_name='autor', on_delete=models.DO_NOTHING, null=True, blank=True)
    publicacao = models.ForeignKey(Publicacao, related_name='publicacao', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto


