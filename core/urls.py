from django.urls import path

from . import views

urlpatterns = [
    path('pessoa/', views.PessoaCreateView.as_view(), name='pessoa'),
    path('endereco/', views.EnderecoCreateView.as_view(), name='endereco'),
]
