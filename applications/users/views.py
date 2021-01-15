from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    View
)
from django.views.generic.edit import (
    FormView
)
from .forms import(
    UserRegisterForm,
    UserLoginForm,
    UserUpdatePasswordForm,
)
    
from .models import User

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['telefono'],
            form.cleaned_data['correo'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            aPaterno = form.cleaned_data['aPaterno'],
            aMaterno = form.cleaned_data['aMaterno'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            direccion = form.cleaned_data['direccion'],
            cp = form.cleaned_data['cp'],
            avisoPrivacidad = form.cleaned_data['avisoPrivacidad'],
        )
        return super(UserRegisterView, self).form_valid(form)

class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
            telefono = form.cleaned_data['telefono'],
            password = form.cleaned_data['password1']
        )
        login(self.request, user)

        return super(UserLoginView, self).form_valid(form)

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