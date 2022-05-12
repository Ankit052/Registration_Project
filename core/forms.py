from calendar import c
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254,help_text="Enter a valid email id ")

    class Meta:
        model = User
        fields = [
            "user_type",
            "first_name",
            "last_name",
            "profile_picture",
            "username",
            "email",
            "password1",
            "password2",
            "address"
        ]