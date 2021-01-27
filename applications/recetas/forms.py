from django import forms
from django.conf import settings
from .models import Receta
from applications.users.models import Paciente


class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.user.nombre, obj.user.aPaterno)


class RecetaForm(forms.ModelForm):

    # fecha = forms.DateField(
    #     input_formats=settings.DATE_INPUT_FORMATS,
    # )

    paciente = CustomModelChoiceField(queryset = Paciente.objects.all())

    class Meta:
        model = Receta
        fields = (
            'fecha',
            'contenido',
        )

        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'data-select':'datepicker',
                    'autocomplete': 'off',
                }
            )
        }
