from rest_framework import serializers

from core.models import Endereco, Pessoa


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        exclude = [
            'id',
            'pessoa'
        ]


class PessoaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'cpf',
            'salario',
            'enderecos',
        ]


class SalarioPessoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'salario',
        ]
