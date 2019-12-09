from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=75)
    descricao_curta = models.TextField(max_length=150)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)# depois tenho que trocar
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(default=0)
    perco_marketing_promocional = models.FloatField(default=0)
    tipo = models