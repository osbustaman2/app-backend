import os
import django
from django import conf
from pymongo import MongoClient
from django.core.management import call_command

from applications.base.models import Cliente

def connection_mongo(cliente):
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.local")
        django.setup()

        nueva_base = {
            'ENGINE': 'djongo',
            'NAME': cliente.data['nombre_bd'],
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': "mongodb://localhost:27017/"
            } 
        }

        nombre_bd = cliente.data['nombre_bd']
        conf.settings.DATABASES[nombre_bd] = nueva_base

        call_command('migrate', database=f'{nombre_bd}'.lower())

    except Exception as err:
        print(f'Error al conectar con el servidor: {err}')
    