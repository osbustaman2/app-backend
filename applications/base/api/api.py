import psycopg2

from django.contrib.auth.models import User

from decouple import config

from rest_framework import generics, status
from rest_framework.response import Response
from applications.base.api.serializer import (
      AddClienteSerializers
    , ClienteSerializers
    , UserSerializer
)

from applications.base.models import Cliente
from applications.base.utils import crearMigrate, create_database, getCliente, validarRut

class ClienteCreateAPIView(generics.CreateAPIView):
    serializer_class = AddClienteSerializers

    def post(self, request, format=None):
        serializer = AddClienteSerializers(data=request.data)
        if serializer.is_valid():
            if not validarRut(request.data['rut_cliente']):
                return Response({
                        "error": "El rut es invalido"
                    }, 
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)

            if getCliente(request.data):
                return Response({
                        "error": "el cliente ya existe"
                    }, 
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)

            ## Guarda los datos del cliente
            serializer.save()

            # Crea la base de datos y su migración
            create_database(request.data)
            crearMigrate(request.data)

            response_to_page = {
                "data_serializer": serializer.data
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClientesListApiView(generics.ListAPIView):
    # Here you get the list of all registred tipo_producto
    serializer_class = ClienteSerializers

    def get_queryset(self):
        get_all_clientes = Cliente.objects.filter(deleted='N')
        return get_all_clientes
    
class ClientesDetailApiView(generics.ListAPIView):
    # Here you get the list of all registred users
    serializer_class = ClienteSerializers

    def get_queryset(self):
        object_marca = Cliente.objects.filter(id=self.kwargs['pk'])
        return object_marca
    
class ClienteRetriveUpdateView(generics.UpdateAPIView):
    # From here a tipo_producto is update 
    serializer_class = ClienteSerializers

    def get_queryset(self, pk):
        return Cliente.objects.filter(id = pk).first()

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if producto_serializer.is_valid():
                producto_serializer.save()


                return Response(producto_serializer.data, status=status.HTTP_200_OK)
            return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClienteDeleteView(generics.DestroyAPIView):
    # From here a tipo_producto is delete 
    serializer_class = ClienteSerializers
    queryset = Cliente.objects.all()

class AdminUserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, pk):
        client = Cliente.objects.get(id=pk)
        database_name = client.nombre_bd

        form = User()

        form.username = request.data['username']
        form.first_name = request.data['first_name']
        form.last_name = request.data['last_name']
        form.email = request.data['email']
        form.set_password(request.data['password'])
        form.is_staff = True
        form.is_superuser = True
        form.save(using=database_name)

        return Response({'success': True}, status=status.HTTP_201_CREATED)



















            
