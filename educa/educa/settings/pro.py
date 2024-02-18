from .base import *

DEBUG = False

ADMINS = (
    ('Pablo C', os.environ['GMAIL_ACCOUNT']),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PG_DB_NAME'],
        'USER': os.environ['PG_USER'],
        'PASSWORD': os.environ['PG_PASSWORD'],
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True