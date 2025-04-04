from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name','email','message']


class Signup_Form(forms.ModelForm):
    username =forms.CharField(label='Username',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    password = forms.CharField(label='Password',max_length=100,required=True)
    password_confirm = forms.CharField(label='Confirm_Password',max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')

            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Password do not match!")

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100,required=True)
    password = forms.CharField(label='Password',max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username,password = password)
            if user is None:
                raise forms.ValidationError("Invalid username and password!")
