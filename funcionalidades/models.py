from django.db import models

# Create your models here.


class Pessoa(models.Model):
    
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome',
    )

    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    idade = models.CharField(
        max_length=255,
        verbose_name='Idade'
    )
    senha = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Partida(models.Model):

    pessoa = models.ForeignKey(
        Pessoa, on_delete=None
    )

    titulo = models.CharField(
        max_length=255, 
        verbose_name='Nome de partida',
        unique=True)

    local = models.TextField(
        verbose_name='Local da sua partida'
    )
    data = models.DateTimeField(
        max_length=255,
        verbose_name='Data'
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.pessoa.nome + ' - ' + self.titulo



