# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

"""
Django settings for gek project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
from django.utils.translation import ugettext_lazy as _

try:
    from common_settings import *
except ImportError:
    INSTALLED_APPS = []

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x92o^!)r-e&&_yhwk2-b%@!v#nz%uhha@jvkvhj)q*egv9&!lm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['gek.com']


# Application definition
INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',

    # origin
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
    'solo',
    'django_filters',
    'multiselectfield',

    # own
    'users',
    'admin2',
    'common',
    'articles',
    'services',
    'rieltor_object',
    'trust',
    'contact',
    'videos',
    'favorites',
    'plan',
    'polls',
    'banners',
    'seo',
    'landing',
    'privat24',
    'liqpayapp',
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gekcom',
        'USER': 'gekcom',
        'PASSWORD': 'gekcom',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'server@whatever.com'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'ru-RU'
LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_ERROR_MESSAGE = _("An error has occurred")

LANGUAGES = (
    ('ru', _('Русский')),
    ('uk', _('Украинский')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

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
                'common.context_processors.counter',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
with open('media_path.json', 'w') as f:
    f.write(json.dumps({'path': MEDIA_ROOT}))

try:
    from local_settings import *
except ImportError:
    pass