from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videollamada/', include('applications.videollamada.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),
    path('', include('pwa.urls')),
]
