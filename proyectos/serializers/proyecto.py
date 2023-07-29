from rest_framework import serializers
from proyectos.models import Proyecto
from proyectos.serializers.categoria import *

from proyectos.serializers.inscritos import *
class ProyectoSerializer(serializers.ModelSerializer):
    # categorias = CategoriaSerializer(many=True)
    # aprendiz = InscritoSerializer()
    # categorias = CategoriaSerializer(many=True)

    class Meta:
        model = Proyecto
        fields = ['id','nombre_proyecto', 'descripcion','aprendiz','codigo_fuente', 'categorias', 'estado','foto']
        
        #fields = ['url', 'id','nombre_proyecto']
