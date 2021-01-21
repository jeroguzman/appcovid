from django.urls import path
from . import views
from .views import send_push, push_home, well
app_name = "home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('send-push/', send_push, name='send-push'),
    path('push-home/', push_home, name='push-home'),
    path('.well-known/pki-validation/ED2FF1C875C44F9BAC2E2B41264C40F0.txt', well, name='well'),


]