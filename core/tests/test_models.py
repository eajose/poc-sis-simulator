from django.test import TestCase

from ..models import Pessoa, Endereco


class PessoaTestCase(TestCase):
    def setUp(self) -> None:
        self.pessoa = Pessoa.objects.create(
            nome="Fulano",
            cpf="999.999.999-99",
            salario=999.99
        )

    def test_str(self):
        self.assertEqual(str(self.pessoa), 'Fulano')


class EnderecoTestCase(TestCase):
    def setUp(self) -> None:
        pessoa = Pessoa.objects.create(
            nome="Fulano",
            cpf="999.999.999-99",
            salario=999.99
        )
        self.endereco = Endereco.objects.create(
            logradouro="Rua dos bobos",
            numero='0',
            bairro='Bairro dos bobos',
            cidade='Cidade dos bobos',
            estado='Bobos',
            pessoa=pessoa,
        )

    def test_str(self):
        self.assertEqual(str(self.endereco), 'Fulano')
