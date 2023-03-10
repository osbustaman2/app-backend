from django.contrib.auth.models import User

from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response

from app.functions import load_one_database
from applications.base.api.serializer import AddClienteSerializers, ClienteSerializers, UserSerializer

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

            return Response(serializer.data, status=status.HTTP_201_CREATED)
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



















    
class UsuarioCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        try:
            id_objeto = request.data['idCliente']
            registros = Cliente.objects.filter(id=id_objeto)

            form = User()
            form.username = request.data['username']
            form.first_name = request.data['first_name']
            form.last_name = request.data['last_name']
            form.email = request.data['email']
            form.set_password(request.data['password'])
            form.is_staff = True
            form.is_superuser = True

            load_one_database(registros)
            form.save(using=registros[0].nombre_bd)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            pass



        # if serializer.is_valid():

        #     id_objeto = request.data['idCliente']
        #     registros = Cliente.objects.filter(id=id_objeto)

        #     serializer.save(using=registros[0].nombre_cliente)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""try:
        cActivo = ClienteActivo.objects.using(la_base.cli_conexion).get(cac_id=la_base.cli_idclienteactivo)
        cActivo.cac_activo = la_base.cli_activa
    except:
        cActivo = ClienteActivo()
        cActivo.cac_rutabase = ''
        cActivo.cac_rutadocumentos = ''
        cActivo.cac_rutadstatic = ''
        cActivo.cac_rutausuarios = ''
        cActivo.cac_nombrebase = la_base.cli_conexion
        cActivo.cac_nombreimagenlogo = ''

    cActivo.save(using=la_base.cli_name)"""
            
