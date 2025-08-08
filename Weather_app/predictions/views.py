from django.shortcuts import render,redirect
from .weather_api import get_weather
from .predictor import predict_weather
from .models import PredictionLog
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def home(request):
    result = None
    we = None
    if request.method == "POST":
        city = request.POST["city"]
        try:
            weather = get_weather(city)
        
            prediction = predict_weather(weather)
            we=PredictionLog.objects.create(
                city=city,
                temperature=weather["temperature"],
                humidity=weather["humidity"],
                wind_speed=weather["wind_speed"],
                pressure=weather["pressure"],
                prediction=prediction
            )
            result = prediction
        except KeyError as e:
            messages.error(request, f"Enter the correct filed: {e}")
        except Exception as e:
            messages.error(request, f"Something went wrong! Try again: {e}")

        
    return render(request, "home.html", {"result": result,"we":we})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
           
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = RegisterForm()
    return render(request, 'Register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request, 'Login successful! You can use the weather prediction.')
                return redirect('home')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request) 
    return redirect('login')  # Redirect to the Home page 