from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.views.generic import(
    View,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import (
    FormView,
)
from .forms import(
    UserRegisterPacienteForm,
    UserRegisterDoctorForm,
    UserLoginForm,
    UserUpdatePasswordForm,
    UserUpdateProfileForm,
)
    
from .models import User

class UserRegisterView(TemplateView):
    template_name = "users/register/register.html"

# class UserRegisterPacienteView(FormView):
#     template_name = 'users/register/register-paciente.html'
#     form_class = UserRegisterPacienteForm
#     success_url = '/'

#     def form_valid(self, form):
#         User.objects.create_user(
#             form.cleaned_data['telefono'],
#             form.cleaned_data['correo'],
#             form.cleaned_data['password1'],
#             nombre = form.cleaned_data['nombre'],
#             aPaterno = form.cleaned_data['aPaterno'],
#             aMaterno = form.cleaned_data['aMaterno'],
#             edad = form.cleaned_data['edad'],
#             sexo = form.cleaned_data['sexo'],
#             direccion = form.cleaned_data['direccion'],
#             cp = form.cleaned_data['cp'],
#             avisoPrivacidad = form.cleaned_data['avisoPrivacidad'],
#         )
#         return super(UserRegisterView, self).form_valid(form)

class UserRegisterPacienteView(FormView):
    template_name = 'users/register/register-paciente.html'
    form_class = UserRegisterPacienteForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'paciente'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_app:home')

class UserRegisterDoctorView(FormView):
    template_name = 'users/register/register-doctor.html'
    form_class = UserRegisterDoctorForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_app:dashboard')

class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        user = authenticate(
            telefono = form.cleaned_data['telefono'],
            password = form.cleaned_data['password1']
        )
        login(self.request, user)
        if self.request.user.is_paciente:
            return redirect('home_app:home')
        else:
            return redirect('home_app:dashboard')


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class UserUpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update-password.html'
    form_class = UserUpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            telefono = usuario.telefono,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['new_password']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)

        return super(UserUpdatePasswordView, self).form_valid(form)

class UserProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users_app:user-profile')
    login_url = reverse_lazy('users_app:user-login')

class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update-profile.html'
    form_class = UserUpdateProfileForm
    success_url = '/'
    login_url = reverse_lazy('users_app:user-login')
    queryset = User.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(User, pk=pk_)

    def form_valid(self, form):
        current_user = self.request.user
        user_to_edit = User.objects.filter(pk=self.kwargs['pk'])

        if user_to_edit.exists() or current_user.is_superuser:
            super(UserUpdateProfileView, self).form_valid(form)
            if self.request.user.is_paciente:
                return redirect('home_app:home')
            else:
                return redirect('home_app:dashboard')
        else:
            return HttpResponseRedirect(
                reverse('users_app:user-logout')
            )