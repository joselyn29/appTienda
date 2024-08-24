from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets #una manera sencilla de crear vistas que manejan operaciones CRUD.
from .models import tbl_producto #modelo 
from .serializers import productoSerializer #El serializador de modelos 



#interfaz completa para gestionar objetos del modelo Evento a través de una API RESTful. Maneja automáticamente las operaciones CRUD utilizando el serializador para convertir datos entre JSON y el modelo Django.
class productoViewSet(viewsets.ModelViewSet):
    queryset = tbl_producto.objects.all()
    serializer_class = productoSerializer

