from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

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

    class Meta:
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


