from .base import *

# False if not in os.environ
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', '192.168.1.173', '178.128.76.91']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbappcovid',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR / 'static')]
#STATIC_ROOT = 'static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

