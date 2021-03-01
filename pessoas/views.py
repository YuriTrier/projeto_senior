from django.views.generic.list import ListView
from pessoas.models import Pessoa

class PessoaListView(ListView):

    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context