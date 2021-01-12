from django.urls import path
from .views import RegisterView

app_name = 'register_app'

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'a-register'),
]