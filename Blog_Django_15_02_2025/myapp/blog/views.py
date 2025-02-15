import logging
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse #for key is revers and named url
from blog.models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages
from django.contrib.auth  import authenticate, login as auth_login, logout

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes #bytes converter
from django.contrib.sites.shortcuts import get_current_site #current sites
from django.template.loader import render_to_string #sting converter
from django.core.mail import send_mail

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
            return redirect('blog:login')
            
        
    return render(request,'blog/register.html',{'form': form})


def Login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                print("Login Success")
                return redirect("blog:dashboard") 
                
    return render(request,'blog/login.html',{'form':form})

def Dashboard(request):
    blog_title = "My Posts"
    return render(request,'blog/dashboard.html',{'blog_title':blog_title})


def Logout(request):
    logout(request)
    return redirect("blog:index") 

def forgot_password(request):
    form = ForgotPasswordForm()
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            #send email to reset password
            token = default_token_generator.make_token(user) #token generator
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            domain = current_site.domain
            subject = "Reset Password Request"
            message = render_to_string('blog/reset_password_email.html',{
                'domain': domain,
                'uid':uid,
                'token':token
            })

            send_mail(subject,message, 'noreplay@praveen.com', [email])
            messages.success(request, 'Email has been sent.')



    return render(request, 'blog/forgot_password.html',{'form':form})

def reset_password(request):
    pass