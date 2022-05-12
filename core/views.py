from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "home.html"
    login_url = reverse_lazy("index")
    

class UserDetails(LoginRequiredMixin,TemplateView):
    model = User
    template_name = "details.html"
    login_url = reverse_lazy("index")
    


class SignUpView(CreateView):
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy("home")
    template_name = "signup.html"

