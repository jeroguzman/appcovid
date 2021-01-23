from django.urls import path
from . import views
from .views import send_push, push_home

app_name = "home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('send-push/', send_push, name='send-push'),
    path('push-home/', push_home, name='push-home'),
]