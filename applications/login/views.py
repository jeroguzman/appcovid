from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LoginForm

class LoginView(TemplateView):
    template_name = 'login/login.html'
