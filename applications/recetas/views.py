from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import(
    FormView,
    TemplateView,
    View,
)
from applications.home.decorators import paciente_required, doctor_required
from appcovid.utils import render_to_pdf
from .forms import RecetaForm
from .models import Receta


# Create your views here.
@method_decorator([login_required, paciente_required], name='dispatch')
class RecetasPacienteView(LoginRequiredMixin, TemplateView):
    model = Receta
    template_name = 'recetas/recetas-paciente.html'
    success_url = reverse_lazy('recetas_app:recetas-paciente')
    login_url = reverse_lazy('users_app:user-login')

    def get(self, request):
        recetas = Receta.objects.filter(paciente_id = self.request.user.id)
        args = {'recetas': recetas}
        return render(request, self.template_name, args)

@method_decorator([login_required, doctor_required], name='dispatch')
class RecetasDoctorView(LoginRequiredMixin, FormView):
    model = Receta
    template_name = 'recetas/recetas-doctor.html'
    form_class = RecetaForm
    success_url = reverse_lazy('recetas_app:recetas-doctor')
    login_url = reverse_lazy('users_app:user-login')

    def get(self, request):
        form = RecetaForm()
        recetas = Receta.objects.filter(doctor_id = self.request.user.id)
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

            subject = 'App Covid | Tu Receta'
            message = 'Adjuntamos un pdf con tu receta'
            from_email = 'correoappcovid@gmail.com'        
            correo_paciente = paciente.user.correo
           
           
            ctx = {
                "doctor": receta.doctor,
                "fecha" : receta.fecha,
                "paciente": receta.paciente,
                "contenido": receta.contenido,
                "firma": receta.doctor.doctor.firma.path
            }
            pdf = render_to_pdf('recetas/receta-pdf.html', ctx)

            email = EmailMultiAlternatives(
                subject,
                message,
                from_email,
                ['galota8686@poetred.com', correo_paciente],
            )
            email.attach("Receta_%s.pdf" %(receta.paciente.user.nombre), pdf, "appliaction/pdf")
            email.send()

            return super(RecetasDoctorView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:user-logout')
            )

class RecetaPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('recetas/receta-pdf.html')
        receta = Receta.objects.get(id = request.GET.get("id"))
        ctx = {
            "doctor": receta.doctor,
            "fecha" : receta.fecha,
            "paciente": receta.paciente,
            "contenido": receta.contenido,
            "firma": receta.doctor.doctor.firma.path
        }
        html = template.render(ctx)
        pdf = render_to_pdf('recetas/receta-pdf.html', ctx)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Receta_%s" %(receta.paciente.user.nombre)
            content = "inline; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("No se encontro la receta")