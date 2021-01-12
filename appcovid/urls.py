from django.contrib import admin
from django.urls import path, include, re_path
from video_app import urls as vdo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include(vdo_urls)),
    re_path('', include('applications.login.urls')),
    re_path('', include('applications.register.urls')),
]
