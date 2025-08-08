from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.book_create, name='book_create'),
]
