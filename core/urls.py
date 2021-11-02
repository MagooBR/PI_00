from django.urls import path

from . views import index, fornecedor

urlpatterns = [
    path('', index, name='index'),
    path('fornecedor/', fornecedor, name='fornecedor'),
]