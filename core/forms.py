from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row
from validate_docbr import CPF

from .models import Pessoa, Endereco


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {
            'cpf': 'CPF'
        }
        localized_fields = ('salario',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Div('nome', css_class="col-6"),
                Div('cpf', css_class="col-6"),
                Div('salario', css_class="col-6"),
            ),
        )

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        validate_cpf = CPF()
        if not validate_cpf.validate(cpf):
            raise forms.ValidationError('O CPF é invalido')

        return cpf


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = '__all__'
        widgets = {
            'pessoa': forms.RadioSelect()
        }
