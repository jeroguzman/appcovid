from django.urls import path, include
from .views import AgoraVideoCall
from . import views

app_name = 'videollamada'

urlpatterns = [
    path('', views.consultorios, name="consultorios"),
    path('consultorio1/', AgoraVideoCall.as_view(app_id='8c9b9f4dde4c46d998166eceb384467a', channel='1'), name='consultorio1'),
    path('consultorio2/', AgoraVideoCall.as_view(app_id='514a20f596134a49a8672b33e2d669e4', channel='2'), name='consultorio2'),
    path('consultorio3/', AgoraVideoCall.as_view(app_id='70539844ec8343bfa86fb756f398d2fd', channel='3'), name='consultorio3'),
    path('consultorio4/', AgoraVideoCall.as_view(app_id='06c474f9a04444e5856953e5276796f8', channel='4'), name='consultorio4')

]

