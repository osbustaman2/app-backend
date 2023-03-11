
from rest_framework import serializers
from django.contrib.auth.models import User
from applications.base.models import Cliente

from rest_framework import serializers
from django.contrib.auth.hashers import make_password   


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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Hashea la contraseña antes de crear el usuario
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)