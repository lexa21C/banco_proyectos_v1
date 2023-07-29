from rest_framework import serializers
from proyectos.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['url','id', 'nombre']
