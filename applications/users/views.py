from django.shortcuts import render
from django.views.generic.edit import (
    FormView
)
from .forms import UserRegisterForm
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