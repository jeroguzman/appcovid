from django.shortcuts import render, get_object_or_404, redirect
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

#UserAuth = get_user_model()

# def home(request):
#     if request.user.is_authenticated:
#         if request.user.is_paciente:
#             return redirect('home_app:home')
#         else:
#             return redirect('home_app:dashboard')
#     return render(request, 'users_app:login')


@method_decorator([login_required, paciente_required], name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):    
        login_url = reverse_lazy('users_app:user-login')
        return render(request, 'home/home.html')
        

@method_decorator([login_required, doctor_required], name='dispatch')
class DashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'home/dashboard.html'
    login_url = reverse_lazy('users_app:user-login')
    queryset = User.objects.all()

