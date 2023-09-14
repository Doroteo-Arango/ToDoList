# Modifications for registration form
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create a class that inhertits from user creation form
class RegisterForm(UserCreationForm):
    # Add attributes
    email = forms.EmailField()
    
    # Allow us to change parent properties of class
    class Meta:
        # Ensure register form will save to user's database
        # Define that we will change user model whenever something in RegisterForm is saved
        model = User
        # Specify the order of attributes
        fields = ["username", "email", "password1", "password2"]