from django.db import models

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=150)
    created_in = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nome

    def update(self, nome, cep, uf, cidade, logradouro, numero, bairro):
        self.nome = nome
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro

        self.save()
