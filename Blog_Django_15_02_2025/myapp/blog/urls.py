from django.urls import path # type: ignore
from . import views 

app_name = 'blog' # for menstioned blow urlpatterns are inside the app_name that is blog.

urlpatterns = [
    path('',views.index, name = "index"),
    path('post/<str:slug>',views.detail, name = "detail"),#dynamic urs<str:>
    path('new_something_url',views.new_url_view, name="new_page_url"),#Redirects, reversed name url also.
    path('old_url',views.old_url_redirect, name ="old_url"),
    path('contact',views.ContactPage, name ="contact"),
    path('about',views.about_view, name ="about"),
    path('register',views.Register, name ="register"),
    path('login',views.Login, name ="login"),
    path('dashboard',views.Dashboard, name ="dashboard"),
    path('logout',views.Logout, name ="logout"),
    path('forgot_password',views.forgot_password, name ="forgot_password"),
    path('reset_password/<uidb64>/<token>',views.reset_password, name ="reset_password"),

]