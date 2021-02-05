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
    UserLoginForm,
    UserUpdatePasswordForm,
    UserUpdateProfileForm,
    UserUpdateFirmaForm,
)
    
from .models import User

class UserRegisterPacienteView(FormView):
    template_name = 'users/register-paciente.html'
    form_class = UserRegisterPacienteForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'paciente'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_app:home')

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
    template_name = 'users/paciente/profile.html'
    success_url = reverse_lazy('users_app:user-profile')
    login_url = reverse_lazy('users_app:user-login')

class UserDoctorProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/doctor/profile.html'
    success_url = reverse_lazy('users_app:user-doctor-profile')
    login_url = reverse_lazy('users_app:user-login')

class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/paciente/update-profile.html'
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


class UserUpdateDoctorProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/doctor/update-profile.html'
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
        doctor = self.request.user.doctor

        if user_to_edit.exists() or current_user.is_superuser:
            doctor.cedula = self.request.POST['cedula']
            doctor.save()
            super(UserUpdateDoctorProfileView, self).form_valid(form)

            if self.request.user.is_paciente:
                return redirect('home_app:home')
            else:
                return redirect('home_app:dashboard')
        else:
            return HttpResponseRedirect(
                reverse('users_app:user-logout')
            )

class UserUpdateDoctorFirmaView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/doctor/update-firma.html'
    form_class = UserUpdateFirmaForm
    success_url = '/'
    login_url = reverse_lazy('users_app:user-login')
    queryset = User.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(User, pk=pk_)

    def form_valid(self, form):
        current_user = self.request.user
        user_to_edit = User.objects.filter(pk=self.kwargs['pk'])
        doctor = self.request.user.doctor

        if user_to_edit.exists() or current_user.is_superuser:
            doctor.firma = self.request.FILES['firma']
            doctor.save()
            super(UserUpdateDoctorFirmaView, self).form_valid(form)

            return redirect('home_app:dashboard')
        else:
            return HttpResponseRedirect(
                reverse('users_app:user-logout')
            )