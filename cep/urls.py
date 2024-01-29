from django.urls import path
from . import views

urlpatterns = [
    path('busca_cep/', views.busca_cep, name='busca_cep'),
]