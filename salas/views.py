from django.views.generic.list import ListView
from salas.models import Salas

class SalasListView(ListView):

    model = Salas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context