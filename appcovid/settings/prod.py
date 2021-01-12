from .base import *

# False if not in os.environ
DEBUG = False

# DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', '192.168.1.173', '178.128.76.91']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbappcovid',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

