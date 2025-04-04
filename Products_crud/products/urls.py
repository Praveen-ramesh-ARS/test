
from django.urls import path
from .views import products_create,products_list,products_update,products_delete

urlpatterns = [
    path('create/',products_create, name='products_create'),
    path('list/',products_list, name='products_list'),
    path('update/<int:pk>/',products_update, name='products_update'),
    path('delete/<int:pk>/',products_delete, name='products_delete'),
]
