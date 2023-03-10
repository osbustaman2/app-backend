import re
import django
from django import conf
import psycopg2
import os

from decouple import config
from django.core.management import call_command
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from applications.base.models import Cliente


def getCliente(request):
    return Cliente.objects.filter(rut_cliente = request['rut_cliente']).exists()

def validarRut(rut):
    rut = rut.replace(".", "").replace("-", "") # Eliminar puntos y guiones
    if not re.match(r'^\d{1,8}[0-9K]$', rut): # Verificar formato
        return False
    rut_sin_dv = rut[:-1]
    dv = rut[-1].upper() # Obtener dígito verificador
    multiplicador = 2
    suma = 0
    for r in reversed(rut_sin_dv):
        suma += int(r) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv_calculado = 11 - resto
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)
    return dv == dv_calculado

def create_database(request):

    ba_nombre = request['nombre_bd']

    try:
        # se crea la conexion
        conexion = psycopg2.connect(
            dbname='postgres', 
            user=config('USER'), 
            host=config('HOST'), 
            password=config('PASSWORD')
        )

        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except Exception as inst:
        return {
            'label': 'DATABASE',
            'error': str(inst),
            'isError': True
        }


    cur = conexion.cursor()
    # se crea la base
    try:
        # se crea la base
        cur.execute("CREATE DATABASE %s ;" % ba_nombre)
    except Exception as inst:
        return {
            'label': 'CREATE DATABASE',
            'error': type(inst),
            'isError': True
        }

    return { 'isError': False }

def crearMigrate(request):

    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app01.settings.local")
        django.setup()

        nombre_bd = request['nombre_bd']

        nueva_base = {
            'ENGINE': conf.settings.DATABASES['default']['ENGINE'],
            'HOST': config('HOST'),
            'NAME': nombre_bd,
            'USER': config('USER'),
            'PASSWORD': config('PASSWORD'),
            'PORT': config('PORT')
        }
        conf.settings.DATABASES[nombre_bd] = nueva_base

        call_command('migrate', database=f'{nombre_bd}'.lower())
    except Exception as err:
        print(f'Error al conectar con el servidor: {err}')

