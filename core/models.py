from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Categoria(models.Model):
    nome = models.CharField('nome', max_length=45)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=45)
    categoria = models.ManyToManyField(Categoria, related_name="tipo")

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nome



class Fornecedor(models.Model):
    tipo=models.ManyToManyField(Tipo, related_name="fornecedor")
    nome = models.CharField('nome', max_length=45)
    endereco = models.CharField('endereco',max_length=255, blank = True)
    telefone=models.CharField('telefone',max_length=13)
    comentario = models.TextField(blank = True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome




