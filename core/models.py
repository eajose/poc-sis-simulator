from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(unique=True, max_length=14)
    salario = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='enderecos'
    )

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self):
        return self.pessoa.nome
