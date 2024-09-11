import os
from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY') or get_random_secret_key()

DEBUG = os.environ.get('DEBUG', '0') == '1'

# Add this to the existing settings.py file
STATIC_URL = '/static/'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth_client',
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

ROOT_URLCONF = 'oauth_client.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'oauth_client/templates')],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

OAUTH2_PROVIDER = {
    'CLIENT_ID': os.environ.get('OAUTH2_PROVIDER_CLIENT_ID'),
    'CLIENT_SECRET': os.environ.get('OAUTH2_PROVIDER_CLIENT_SECRET'),
    'AUTHORIZATION_URL': os.environ.get('OAUTH2_PROVIDER_AUTHORIZATION_URL'),
    'TOKEN_URL': os.environ.get('OAUTH2_PROVIDER_TOKEN_URL'),
    'REDIRECT_URL': os.environ.get('OAUTH2_PROVIDER_REDIRECT_URL'),
    'SCOPE': 'read write',
}
