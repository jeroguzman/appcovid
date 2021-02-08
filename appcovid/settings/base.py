from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parents[2]
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x5mx=-frw*(3rq9d8+__2ndj5w#=wy(9qk)4pd8v^ke3e^k7vn'

# SECURITY WARNING: don't run with debug turned on in production!
CORS_ORIGIN_ALLOW_ALL = True
SITE_ID = 1

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
)

LOCAL_APPS = (
    'applications.videollamada',
    'applications.home',
    'applications.users',
    'applications.recetas',
    'applications.blog',
)

THIRD_PARTY_APPS = (
    'corsheaders',
    'pwa',
    'commonstuff',
    'push',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'appcovid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'static/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'appcovid.wsgi.application'

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



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
DATE_INPUT_FORMATS = ('%d-%m-%Y')

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'correoappcovid@gmail.com' 
EMAIL_HOST_PASSWORD = 'Appcovid21'
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DJANGO_INFOPUSH_VAPID_PUBLIC_KEY = "BIAdqGnd66Ets5M7qF4mDOAWxW0INzY9OlVRbCM3TL7Gj-7Z_tvTx7KVtNr83-D6X_bgFQKyHyhQXd8bW7uZxYc"
DJANGO_INFOPUSH_VAPID_PRIVATE_KEY = "k41zAAVnfMgZw2fQY_3yc35f_M7o7SKTpR7qBbceQtc"
DJANGO_INFOPUSH_VAPID_ADMIN_EMAIL = "jeroguzman@gmail.com"

PWA_APP_NAME = 'App Covid' 
PWA_APP_DESCRIPTION = "Municipio de Nogales 2018-2021" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#ffffff' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'portrait' 
PWA_APP_START_URL = '/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ 
    { 
        'src': '/static/img/pwa/logo-nogales-16.png', 
        'sizes': '160x160' 
    } 
] 
PWA_APP_ICONS_APPLE = [ 
    { 
        'src': '/static/img/pwa/logo-nogales-16.png', 
        'sizes': '160x160' 
    } 
] 
PWA_APP_SPLASH_SCREEN = [ 
    { 
        'src': '/static/img/pwa/icons/logo-nogales-16.png', 
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)' 
    } 
] 
PWA_APP_DIR = 'static/' 
PWA_APP_LANG = 'es-MX'
PWA_APP_DEBUG_MODE = False
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/', 'serviceworker.js')


'''Social Login

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_FACEBOOK_KEY = '4091407147545355'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c324a252f8d8f39031681011bb03cf73'

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['last_name', 'first_name', 'email']'''
