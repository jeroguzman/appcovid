from django.urls import path
from .views import LoginView

app_name = 'login_app'

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'a-login'),
]