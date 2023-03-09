
from rest_framework import serializers
from django.contrib.auth.models import User
from applications.base.models import Cliente


class AddClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'nombre_cliente', 
            'rut_cliente', 
            'nombre_bd', 
            'fecha_ingreso', 
            'fecha_termino', 
            'cantidad_usuarios'
        )

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')


class UserSerializer(serializers.Serializer):
    idCliente = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    # class Meta:
    #     model = User
    #     fields = ('idCliente', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
