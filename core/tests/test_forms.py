from django.test import TestCase


from ..models import Pessoa
from ..forms import PessoaForm, EnderecoForm


class PessoaFormTest(TestCase):
    def setUp(self) -> None:
        self.data = {
            'nome': 'Fulano',
            'cpf': '782.328.690-46',
            'salario': 999.99
        }

    def test_save(self):
        form = PessoaForm(self.data)
        form.is_valid()
        pessoa = form.save()

        self.assertIsNotNone(pessoa.pk)

    def test_save_sem_commit(self):
        form = PessoaForm(self.data)
        form.is_valid()
        pessoa = form.save(commit=False)

        self.assertIsNone(pessoa.pk)

    def test_cpf_invalido(self):
        form = PessoaForm({'cpf': '000.000.000-00'})

        self.assertIn('O CPF é invalido', form.errors['cpf'])

    def test_cpf_ja_existe(self):
        Pessoa.objects.create(
            nome='Fulano',
            cpf='782.328.690-46',
            salario=999.99
        )

        form = PessoaForm(self.data)

        self.assertIn('Pessoa com este Cpf já existe.', form.errors['cpf'])


class EnderecoFormTest(TestCase):
    def setUp(self) -> None:
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
            'pessoa': pessoa,
        }

    def test_save(self):
        form = EnderecoForm(self.data)
        form.is_valid()
        endereco = form.save()

        self.assertIsNotNone(endereco.pk)

    def test_save_sem_commit(self):
        form = EnderecoForm(self.data)
        form.is_valid()
        endereco = form.save(commit=False)

        self.assertIsNone(endereco.pk)
