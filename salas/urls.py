from django.urls import path

from salas.views import SalasListView

urlpatterns = [
    path('', SalasListView.as_view(), name='salas-list'),
]