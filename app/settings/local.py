import os
from .base import *

from decouple import config

DEBUG = True

ALLOWED_HOSTS = ["*"]
PORT_LOCALHOST = '8080'
NAME_HOST = 'rasuz.algo'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('DB_NAME'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': config('HOST')
        } 
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

