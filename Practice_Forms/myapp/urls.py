from django.urls import path

from .views import *
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
