from rest_framework import serializers
from .models import tbl_producto

# Serializador para manejar datos json 
class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_producto
        #los datos que se van a convertir a Json o al contrario, en este caso todo ('__all__')
        fields = '__all__' 