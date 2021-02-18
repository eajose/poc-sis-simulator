from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import PessoaForm, EnderecoForm
from .models import Pessoa, Endereco
# Create your views here.


class PessoaCreateView(CreateView):
    model = Pessoa
    template_name = "core/pessoa.html"
    form_class = PessoaForm
    success_url = reverse_lazy('pessoa')


class EnderecoCreateView(CreateView):
    model = Endereco
    template_name = "core/endereco.html"
    form_class = EnderecoForm
    success_url = reverse_lazy('endereco')
