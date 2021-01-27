from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    FormView,
    TemplateView
)
from .forms import RecetaForm
from .models import Receta


# Create your views here.
class RecetasPacienteView(LoginRequiredMixin, TemplateView):
    model = Receta
    template_name = 'recetas/recetas-paciente.html'
    success_url = reverse_lazy('recetas_app:recetas-paciente')
    login_url = reverse_lazy('users_app:user-login')

    def get(self, request):
        recetas = Receta.objects.filter(paciente_id = self.request.user.id)
        args = {'recetas': recetas}
        return render(request, self.template_name, args)

class RecetasDoctorView(LoginRequiredMixin, FormView):
    model = Receta
    template_name = 'recetas/recetas-doctor.html'
    form_class = RecetaForm
    success_url = reverse_lazy('recetas_app:recetas-doctor')
    login_url = reverse_lazy('users_app:user-login')

    def get(self, request):
        form = RecetaForm()
        recetas = Receta.objects.all()
        args = {'form':form, 'recetas': recetas}
        return render(request, self.template_name, args)

    def form_valid(self, form):
        current_user = self.request.user
        paciente = form.cleaned_data['paciente']
        fecha = form.cleaned_data['fecha']
        contenido = form.cleaned_data['contenido']

        if current_user.is_doctor:
            receta = Receta.objects.create(
                doctor = current_user,
                paciente = paciente,
                fecha = fecha,
                contenido = contenido,
            )
            receta.save()

            return super(RecetasView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:user-logout')
            )

