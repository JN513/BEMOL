from django.db import models

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    #cpf = models.IntegerField()
    cep = models.FloatField()
    uf = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=150)
    #complemento = models.CharField(max_length=150)

    

