from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre',
                    'class': 'form-control',
                }
            ),
            'aPaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Paterno',
                    'class': 'form-control',
                }
            ),
            'aMaterno': forms.TextInput(
                attrs={
                    'placeholder' : 'Apellido Materno',
                    'class': 'form-control',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'placeholder' : 'Edad',
                    'class': 'form-control',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'placeholder' : 'Sexo',
                    'class': 'form-control',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'placeholder' : 'Dirección',
                    'class': 'form-control',
                }
            ),
            'cp': forms.NumberInput(
                attrs={
                    'placeholder' : 'Código Postal',
                    'class': 'form-control',
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'placeholder' : 'Teléfono',
                    'class': 'form-control',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo',
                    'class': 'form-control',
                }
            ),
            'contrasena': forms.PasswordInput(
                attrs={
                    'placeholder' : 'Contraseña',
                    'class': 'form-control',
                }
            ),
            'contrasena2': forms.PasswordInput(
                attrs={
                    'placeholder' : 'Repita su contraseña',
                    'class': 'form-control',
                }
            ),
            'avisoPrivacidad': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
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
            'contrasena': '',
            'contrasena2': '',
            'avisoPrivacidad': 'He leido el aviso de privacidad',
        }


    ##borrar####
    def clean_cp(self):
        cp = self.cleaned_data['cp']
        if cp < 50000:
            raise forms.ValidationError('Ingrese un código postal válido')
        return cp