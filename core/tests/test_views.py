from django.test import TestCase
from django.urls import reverse

from ..models import Pessoa, Endereco


class PessoaViewTestCase(TestCase):
    def setUp(self) -> None:
        self.url = reverse('pessoa')
        self.response = self.client.get(self.url)

    def test_reverse(self):
        self.assertEqual(self.url, '/pessoa/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/pessoa.html')

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(
            self.url,
            {
                'nome': 'Fulano',
                'cpf': '782.328.690-46',
                'salario': 999.99
            }
        )
        self.assertEqual(str(Pessoa.objects.last()), "Fulano")


class EnderecoViewTestCase(TestCase):
    def setUp(self) -> None:
        self.url = reverse('endereco')
        self.response = self.client.get(self.url)
        pessoa = Pessoa.objects.create(
            nome="Fulano",
            cpf="999.999.999-99",
            salario=999.99
        )
        self.data = {
            'logradouro': "Rua dos bobos",
            'numero': '0',
            'bairro': 'Bairro dos bobos',
            'cidade': 'Cidade dos bobos',
            'estado': 'Bobos',
            'pessoa': pessoa.id,
        }

    def test_reverse(self):
        self.assertEqual(self.url, '/endereco/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/endereco.html')

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(
            self.url,
            self.data
        )
        self.assertEqual(str(Endereco.objects.last()), "Fulano")
