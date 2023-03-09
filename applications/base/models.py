from django.db import models
from django.contrib.auth.models import AbstractUser

from djongo import models
from model_utils.models import TimeStampedModel

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from app.settings.local import NAME_HOST, PORT_LOCALHOST

class Cliente(TimeStampedModel):
    OPCIONES = (
        ('S', 'SI'),
        ('N', 'NO'),
    )

    nombre_cliente = models.CharField('Nombre del cliente', max_length=120)
    rut_cliente = models.CharField('Rut del cliente', max_length=20)
    nombre_bd = models.CharField('Nombre base de datos', max_length=20)
    # url_cliente = models.TextField('URL cliente', blank=True, null=True)
    cli_link = models.CharField("Link base", max_length=255, default='')
    imagen_cliente = models.ImageField('Logo Cliente', blank=True, null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    favicon_cliente = models.ImageField('Favicon Cliente', blank=True, null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    cliente_activo = models.CharField("Cliente activo", max_length=1, choices=OPCIONES, default="N", null=True, blank=True)
    fecha_ingreso = models.DateField("Fecha creación de la base", null=True, blank=True)
    fecha_termino = models.DateField(verbose_name='Fecha termino de la base', null=True, blank=True)
    cantidad_usuarios = models.IntegerField("Cantidad usuarios", null=True, blank=True)
    deleted = models.CharField('deleted', max_length=1, choices=OPCIONES, default='N', null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre_cliente

    def __create_url_client(self):
        return f"http://{self.nombre_bd}.{NAME_HOST}:{PORT_LOCALHOST}"

    # def __create_url_client(self):
    #     return ""

    create_url_client = property(__create_url_client)

    def save(self, *args, **kwargs):
        self.cli_link = self.create_url_client.lower()
        super(Cliente, self).save(*args, **kwargs)

    class Meta:
        db_table = 'cliente'
        ordering = ['id']
        unique_together = ('rut_cliente',)
