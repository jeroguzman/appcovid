from django.shortcuts import render
from django.views.generic import(
    FormView,
)
from .forms import RecetaForm


# Create your views here.
class RecetasView(FormView):
    template_name = 'recetas/recetas.html'
    form_class = RecetaForm
    success_url = '/'