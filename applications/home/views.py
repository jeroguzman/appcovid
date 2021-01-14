from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView
)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('users_app:user-login')
