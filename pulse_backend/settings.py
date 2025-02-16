"""
Django settings for pulse_backend project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# TODO: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!8ab1!8@b*+jn*$+tq+0q&8+3i6bsq&fzfg@26d(=55=(d3__h'

DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['*']

SITES_DOMAINS = [
    "https://pulse-work.ru",
]

if DEBUG:
    SITES_DOMAINS += [
        "http://localhost:3000",
    ]


CORS_ALLOWED_ORIGINS = SITES_DOMAINS
CORS_ORIGIN_WHITELIST = SITES_DOMAINS
CSRF_TRUSTED_ORIGINS = SITES_DOMAINS
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "www-authenticate",
]
CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_CREDENTIALS = True

# Application definition

ELC_TOKEN = 'BVMACqY9GvtoX54w24pVeYNKQcMHjPXxzhLVt3NV'
ELC_ID = 30
ELC_STATE = 'https://hackathon-9.orb.ru/backend/auth/ELC'
ELC_REDIRECT = 'https://hackathon-9.orb.ru/panel/auth/login'

INSTALLED_APPS = [
    'jet', # Admin Theme
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'corsheaders',
    'storages',

    'account',
    'person',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            'access_key': '8NG38OE6JC6G4WQPR5BX',
            'secret_key': 'iyl2ookC7H3o1Dx1i6FYABg4TahclKaxis1NPB9a',
            'bucket_name': '42d8bf36-047de542-227f-4fc0-ab34-af47e3d49b7e',
            'endpoint_url': 'https://s3.timeweb.cloud',
            'region_name': 'ru-1',
            'file_overwrite': True,
            'use_ssl': False,
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

GRAPHENE = {
    'SCHEMA': 'pulse_backend.schema.schema',
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
        # 'graphene_django.views.GraphQLView.as_view(csrf_exempt=True)',
    ],
}

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'pulse_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pulse_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = "backend/static/"
if DEBUG:
    STATICFILES_DIRS = ['static']
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = '/mediafiles/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
