from .base import *

# False if not in os.environ
DEBUG = False

# DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', '178.128.76.91']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'appcovid_db',
        'USER': 'appcovid',
        'PASSWORD': 'pitic2020',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
]

