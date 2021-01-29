from django import forms
from django.conf import settings
from .models import Receta
from applications.users.models import Paciente


class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
        return "%s %s %s" % (obj.user.aPaterno, obj.user.aMaterno, obj.user.nombre)

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
