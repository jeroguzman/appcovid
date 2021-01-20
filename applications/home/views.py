from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import paciente_required, doctor_required
from applications.users.models import User
from django.views.generic import (
    TemplateView,
    ListView,
)

# Notificaciones Push Imports
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from webpush import send_user_notification
import json

@method_decorator([login_required, paciente_required], name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('users_app:user-login')

@method_decorator([login_required, doctor_required], name='dispatch')
class DashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'home/dashboard.html'
    login_url = reverse_lazy('users_app:user-login')
    queryset = User.objects.all()

#Notificaciones Push Views

@require_GET
def push_home(request):             
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    return render(request, 'push-home.html', {user: user, 'vapid_key': vapid_key})


@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})
