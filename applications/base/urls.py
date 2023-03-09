from django.urls import path
from applications.base.api.api import (
    ClienteCreateAPIView, 
    ClientesListApiView, 
    UsuarioCreateAPIView, 
    ClienteRetriveUpdateView,
    ClienteDeleteView,
    ClientesDetailApiView
)

app_name = 'base_app'

# http://127.0.0.1:8080/api/register/admin/63d0a8114e577b47d687ae86/
urlpatterns = [
    path('api/add/cliente/', ClienteCreateAPIView.as_view(), name='add-cliente'),
    path('api/edit/cliente/<pk>/', ClienteRetriveUpdateView.as_view(), name='edit-cliente'), 
    path('api/delete/cliente/<pk>/', ClienteDeleteView.as_view(), name='delete-cliente'), 
    path('api/detail/clientes/<pk>/', ClientesDetailApiView.as_view(), name='detail-cliente'),  
    path('api/get/all/clientes/', ClientesListApiView.as_view(), name='get-all-clientes'),   

    
    path('api/register/admin/', UsuarioCreateAPIView.as_view(), name='register-admin'),                                  
]
