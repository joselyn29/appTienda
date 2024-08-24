from django.urls import path, include #funciones para las urls 
from rest_framework.routers import DefaultRouter #rutas basada en viewset 
from .views import productoViewSet # Views.py



router = DefaultRouter() #genera auntomaticamente las rutas 
router.register(r'productos', productoViewSet) #registrando el sujeto en el que se basaran las rutas

# incluyen las rutas generadas por la línea de código arriba
urlpatterns = [
    path('', include(router.urls)),
]
