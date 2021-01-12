from django.urls import path, include
from agora.views import Agora
from . import views

app_name = 'videollamada'

urlpatterns = [
    path('', views.videollamada, name="videollamada"),
    path('success/', views.success, name="success"),
    path('medico1/', Agora.as_view(app_id='8c9b9f4dde4c46d998166eceb384467a', channel='test'), name='medico1')

]

