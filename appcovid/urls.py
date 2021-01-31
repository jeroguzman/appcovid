from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('videollamada/', include('applications.videollamada.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.recetas.urls')),
    path('blog/', include('applications.blog.urls')),
    path('', include('pwa.urls')),
    url(r'^push/', include('push.urls')),
    url(r'^service-worker.js$', cache_page(1 if settings.DEBUG else 86400)(TemplateView.as_view(
        template_name="push/service-worker.js",
        content_type='application/javascript; charset='+settings.DEFAULT_CHARSET,
    )), name='service-worker.js'),
]