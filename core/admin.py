from django.contrib import admin

from .models import Pessoa, Endereco


class EnderecoInLine(admin.TabularInline):
    model = Endereco


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [EnderecoInLine]
