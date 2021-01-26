from django import forms
from django.conf import settings
from .models import Receta

class RecetaForm(forms.ModelForm):

    # fecha = forms.DateField(
    #     input_formats=settings.DATE_INPUT_FORMATS,
    # )

    class Meta:
        model = Receta
        fields = (
            'paciente',
            'fecha',
            'contenido',
        )

        widgets = {
            'fecha': forms.DateInput(
                format = '%d-%m-%Y',
                attrs={
                    'data-select':'datepicker',
                }
            )
        }
