from django.contrib import admin
from django.urls import path, include
from pessoas import urls as pessoas_urls 
from salas import urls as salas_urls 

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pessoas/', include(pessoas_urls)),
    path('salas/', include(salas_urls)),
]
