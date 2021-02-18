from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)

from core.models import Pessoa, Endereco
from .permissions import GrupoApi1
from .serializers import PessoaSerializer, SalarioPessoaSerializer


class PessoaViewSet(ModelViewSet):

    queryset = (
        Pessoa
        .objects
        .all()
    )
    serializer_class = PessoaSerializer


class SalarioViewSet(ModelViewSet):

    queryset = (
        Pessoa
        .objects
        .all()
    )

    serializer_class = SalarioPessoaSerializer
