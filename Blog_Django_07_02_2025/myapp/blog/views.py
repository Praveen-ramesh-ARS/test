from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse #for key is revers and named url
from blog.models import *

# Create your views here.

def index(request):
    # posts=[
    #     {'id':1, 'title':'post 1', 'content':'Content of Post 1'},
    #     {'id':2, 'title':'post 2', 'content':'Content of Post 2'},
    #     {'id':3, 'title':'post 3', 'content':'Content of Post 3'},
    #     {'id':4, 'title':'post 4', 'content':'Content of Post 4'},
    # ]
    blog_title = "Latest Posts"
    posts=Post.objects.all()
    return render(request,'blog/index.html',{'blog_title': blog_title,'posts': posts})

def detail(request,slug):
    try:
        
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
        
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exists!")

    return render(request,'blog/detail.html',{'post':post, 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))#mentioned the new_url of name value name=new_page_url.

def new_url_view(request):
    return HttpResponse('This is the new URL.')