import django.conf as conf
from decouple import config

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
        nueva_base['ENGINE'] = config('ENGINE')
        nueva_base['HOST'] = config('HOST')
        nueva_base['NAME'] = base.nombre_bd
        nueva_base['USER'] = config('USER')
        nueva_base['PASSWORD'] = config('PASSWORD')
        nueva_base['PORT'] = config('PORT')

        conf.settings.DATABASES[subdomain] = nueva_base
