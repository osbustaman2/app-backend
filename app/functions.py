import django.conf as conf

from applications.base.models import Cliente
from app.settings.local import DATABASES


def elige_choices(obj_choice, str):
    valor = ""
    for key, value in obj_choice:
        if key == str:
            valor = value
    return valor

def load_data_base():
    # lista = {}
    lista = Cliente.objects.using('default').all()

    for base in lista:

        domain = base.cli_link
        subdomain = (domain.split('.')[0]).split('//')[1]

        nueva_base = {}
        nueva_base['ENGINE'] = conf.settings.DATABASES['default']['ENGINE']
        nueva_base['NAME'] = base.cli_name
        nueva_base['ENFORCE_SCHEMA'] = False
        nueva_base['CLIENT'] = {
            'host': conf.settings.DATABASES['default']['CLIENT']['host']
        }

        conf.settings.DATABASES[subdomain] = nueva_base


def load_one_database(base):

    try:
        nueva_base = {}
        nueva_base['ENGINE'] = conf.settings.DATABASES['default']['ENGINE']
        nueva_base['NAME'] = base[0].nombre_bd
        nueva_base['ENFORCE_SCHEMA'] = False
        nueva_base['CLIENT'] = {
            'host': conf.settings.DATABASES['default']['CLIENT']['host']
        }

        DATABASES[base.nombre_bd] = nueva_base

    except:
        pass
