"""
Django settings for admitad_test project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yz9%mp_jbf-$c-u+&q&1_5_)!ks10r-*j-fqpchwm#4w(&+a1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pdf_generator',
]

MIDDLEWARE = []

ROOT_URLCONF = 'admitad_test.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'TEST_REQUEST_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/2.2/howto/static-files/
#
STATIC_URL = '/static/'
REPORT_ROOT = os.path.join(BASE_DIR, os.getenv('REPORT_ROOT', 'reports'))
REPORT_URL = '/reports/'

ATTACHMENTS_ROOT = os.path.join(BASE_DIR, os.getenv('ATTACHMENTS_ROOT', 'attached_files'))

MEDIA_ROOT = ATTACHMENTS_ROOT

# overrides test runner to avoid creating test DB
TEST_RUNNER = 'pdf_generator.test_runner.NoDbTestRunner'

###########
#
# Celery config
#
##########
BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_MAX_RETRIES = 5

CELERY_RETRY_COUNTDOWN = 60  # 1 minute

CELERY_ALWAYS_EAGER = False

#########
#
#  Logging
#
#########

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'generation': {
            'format': '%(asctime)s  %(message)s',
        }
    },
    'handlers': {
        'generation': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/generation_logs.log',
            'formatter': 'generation',
        }
    },
    'loggers': {
        'generation': {
            'handlers': ['generation', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
