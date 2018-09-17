from django.db import models
from django.utils import timezone

class Produto(models.Model) :
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    def __str__(self):
       return self.descricao

class Marca(models.Model) :
    nomeMarca = models.CharField(max_length=25)

    def __str__(self):
       return self.nomeMarca
