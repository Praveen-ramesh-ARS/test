from django.shortcuts import render,redirect
from .forms import ContactForm,Signup_Form,LoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate

# Create your views here.


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        

        if form.is_valid():
            form.save()
            messages.success(request,"Message has been sent..!")
        else:
            messages.error(request,'Please Enter correct fields..')

    return render(request, "contact_page.html",{'form': form})

def signup(request):
    form = Signup_Form()
    if request.method == "POST":
        form = Signup_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Registration Successfull!. You can Login!')
            return redirect('myapp:login')

    return render(request,'signup.html',{'form':form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request, "Login sucessfully!")
                return redirect('myapp:index')
            else:
                messages.error(request,"username and password does not match!")

    return render(request,'login.html',{'form':form})

def logout(request):
    auth_logout(request)
    
    return redirect('myapp:index')

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')