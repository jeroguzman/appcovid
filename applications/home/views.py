from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import paciente_required, doctor_required
from applications.users.models import User
from django.views.generic import (
    TemplateView,
    ListView,
)

@method_decorator([login_required, paciente_required], name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('users_app:user-login')

@method_decorator([login_required, doctor_required], name='dispatch')
class DashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'home/dashboard.html'
    login_url = reverse_lazy('users_app:user-login')
    queryset = User.objects.all()