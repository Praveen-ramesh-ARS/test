import logging
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse #for key is revers and named url
from blog.models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    # posts=[
    #     {'id':1, 'title':'post 1', 'content':'Content of Post 1'},
    #     {'id':2, 'title':'post 2', 'content':'Content of Post 2'},
    #     {'id':3, 'title':'post 3', 'content':'Content of Post 3'},
    #     {'id':4, 'title':'post 4', 'content':'Content of Post 4'},
    # ]
    blog_title = "Latest Posts"
    all_posts=Post.objects.all()
    #paginator
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blog/index.html',{'blog_title': blog_title,'page_obj': page_obj})

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

def ContactPage(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = 'Your email has been sent!'
            return render(request, 'blog/contact.html',{'form':form, 'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request, 'blog/contact.html',{'form':form, 'name':name, 'email':email,'message':message})
    return render(request,'blog/contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content' : about_content})

def Register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False) #commit = Flase means not saved all values is set to form variable
            user.set_password(form.cleaned_data['password'])
            user.save()
            # print('Register Successfully!')
            messages.success(request,'Registration Successfull. You can log in.')
            
        
    return render(request,'blog/register.html',{'form': form})