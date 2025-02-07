from django.urls import path # type: ignore
from . import views 

app_name = 'blog' # for menstioned blow urlpatterns are inside the app_name that is blog.

urlpatterns = [
    path('',views.index, name = "index"),
    path('post/<str:slug>',views.detail, name = "detail"),#dynamic urs<str:>
    path('new_something_url',views.new_url_view, name="new_page_url"),#Redirects, reversed name url also.
    path('old_url',views.old_url_redirect, name ="old_url"),

]