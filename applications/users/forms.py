from django import forms
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User, Paciente, Doctor

class UserRegisterPacienteForm(UserCreationForm):
    password1 = forms.CharField(
        label = '',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña',
            }
        )
    )
    password2 = forms.CharField(
        label = '',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Repetir Contraseña',
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        #nombre, apellido paterno, apellido materno, edad, sexo, direccion, cp, telefono, correo, contrasena, confirmar contrasena, aviso de privacidad
        model = User
        fields = (
            'nombre',
            'aPaterno',
            'aMaterno',
            'edad',
            'sexo',
            'direccion',
            'cp',
            'telefono',
            'correo',
            'avisoPrivacidad',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'aPaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Paterno',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'aMaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Materno',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'placeholder' : 'Edad',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'placeholder' : 'Sexo',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'placeholder' : 'Dirección',
                }
            ),
            'cp': forms.TextInput(
                attrs={
                    'placeholder' : 'Código Postal',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder' : 'Teléfono',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo',
                }
            ),
            'avisoPrivacidad': forms.CheckboxInput(
            ),
        }

        labels = {
            'nombre': '',
            'aPaterno': '',
            'aMaterno': '',
            'edad': '',
            'direccion': '',
            'cp': '',
            'telefono': '',
            'correo': '',
            'avisoPrivacidad': 'He leido el aviso de privacidad',
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_paciente = True
        user.nombre = self.cleaned_data.get('nombre')
        user.aPaterno = self.cleaned_data.get('aPaterno')
        user.aMaterno = self.cleaned_data.get('aMaterno')
        user.edad = self.cleaned_data.get('edad')
        user.sexo = self.cleaned_data.get('sexo')
        user.direccion = self.cleaned_data.get('direccion')
        user.cp = self.cleaned_data.get('cp')
        user.avisoPrivacidad = self.cleaned_data.get('avisoPrivacidad')
        user.save()
        paciente = Paciente.objects.create(user=user)
        return user

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', 'Las contraseñas no coinciden')


class UserLoginForm(forms.Form):
    telefono = forms.CharField(
        label = '',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Teléfono',
            }
        )
    )
    password1 = forms.CharField(
        label = '',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        telefono = self.cleaned_data['telefono']
        password1 = self.cleaned_data['password1']

        if not authenticate(telefono = telefono, password = password1):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        
        return self.cleaned_data

class UserUpdatePasswordForm(forms.Form):

        telefono = forms.CharField(
            label = '',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'placeholder' : 'Teléfono',
                }
            )
        )

        password1 = forms.CharField(
            label = '',
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder' : 'Contraseña Actual',
                }
            )
        )
        new_password = forms.CharField(
            label = '',
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder' : 'Contraseña Nueva',
                }
            )
        )

        confirm_new_pass = forms.CharField(
            required=True,
            widget=forms.PasswordInput(
                attrs={'placeholder': 'Confirmar Nueva Contraseña'}
            )
        )

        def clean(self):
            cleaned_data = super(UserUpdatePasswordForm, self).clean()
            telefono = self.cleaned_data['telefono']
            password1 = self.cleaned_data['password1']

            if not authenticate(telefono = telefono, password = password1):
                raise forms.ValidationError('Los datos del usuario no son correctos')
            
            return self.cleaned_data

        def clean_confirm_new_pass(self):
            if self.cleaned_data['new_password'] != self.cleaned_data['confirm_new_pass']:
                self.add_error('confirm_new_pass', 'Las contraseñas actualizadas no coinciden')

class UserUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'nombre',
            'aPaterno',
            'aMaterno',
            'edad',
            'sexo',
            'direccion',
            'cp',
            'telefono',
            'correo',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'aPaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Paterno',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'aMaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Materno',
                    'onkeydown' : 'return alphaOnly(event);',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'placeholder' : 'Edad',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'placeholder' : 'Sexo',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'placeholder' : 'Dirección',
                }
            ),
            'cp': forms.TextInput(
                attrs={
                    'placeholder' : 'Código Postal',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder' : 'Teléfono',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo',
                }
            ),
        }

        labels = {
            'nombre': '',
            'aPaterno': '',
            'aMaterno': '',
            'edad': '',
            'direccion': '',
            'cp': '',
            'telefono': '',
            'correo': '',
        }

class UserUpdateFirmaForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'firma',
        )

        widgets = {
            'firma': forms.FileInput(
                attrs={
                    'id' : 'choose',
                    'class' : 'file-upload-img',
                    'placeholder' : 'Firma',                    
                }
            ),
        }

        labels = {
            'firma': '',
        }
