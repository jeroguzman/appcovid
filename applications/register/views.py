from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import RegisterForm
from .models import User

# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'register/register.html'
    form_class = RegisterForm
    success_url = '/video'