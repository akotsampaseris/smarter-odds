import os
from configparser import RawConfigParser

from pathlib import Path
from datetime import timedelta
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

config = RawConfigParser()
config.read(BASE_DIR / 'smarter_odds/settings.ini')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('debug', 'DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd-Party Apps
    'crispy_forms',
    # Custom Apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smarter_odds.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'smarter_odds.wsgi.application'


# Email Server Setup
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_PORT = config.getint('email', 'EMAIL_PORT')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config.getboolean('email', 'EMAIL_USE_TLS')

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if config.get('db', 'ENGINE') != 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + config.get('db', 'ENGINE'),
            'NAME': config.get('db', 'NAME'),
            'USER': config.get('db', 'USER'),
            'PASSWORD': config.get('db', 'PASSWORD'),
            'HOST': config.get('db', 'HOST'),
            'PORT': config.get('db', 'PORT')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + config.get('db', 'ENGINE'),
            'NAME': BASE_DIR / config.get('db', 'NAME')
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,  'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
