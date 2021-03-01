from django.urls import path

from pessoas.views import PessoaListView

urlpatterns = [
    path('', PessoaListView.as_view(), name='pessoa-list'),
]