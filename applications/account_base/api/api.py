from datetime import datetime

from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from applications.account_base.api.serializer import CustomTokenObtainPairSerializer, CustomUserSerializer

from django.contrib.auth.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)

                request.session['token'] = login_serializer.validated_data.get('access')
                request.session['refresh'] = login_serializer.validated_data.get('refresh')
                request.session['user'] = user_serializer.data

                return Response({
                    'token': request.session['token'],
                    'refresh-token': request.session['refresh'],
                    'user': request.session['user'],
                    'message': 'Inicio de sesion exitosa'
                }, status=status.HTTP_200_OK)
            return Response({
                'error': 'Contraseña o nombre de usuario incorrectos'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'error': 'Contraseña o nombre de usuario incorrectos'
            }, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', ''))
        if user.exists():
            RefreshToken.for_user(user.first)
            return Response({
                'message': 'Sesion cerrada con exito'
            }, status=status.HTTP_200_OK)
        return Response({
                'message': 'No existe este usuario'
            }, status=status.HTTP_400_BAD_REQUEST)
    

