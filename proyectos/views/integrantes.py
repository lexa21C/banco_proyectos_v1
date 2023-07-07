from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

from proyectos.views.funciones import *

class IntegrantesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_integrantes(self, request, *args, **kwargs):
        grupo_id = kwargs['grupo_id']
        # Obtener el id del grupo de los argumentos de la solicitud 

        # Obtener los inscritos que pertenecen al grupo
        inscritos = Inscrito.objects.filter(nombre_grupo_id=grupo_id)

        # Serializar los datos de los inscritos
        serializer = self.get_serializer(inscritos, many=True)

        # Devolver la respuesta con los datos serializados
        return Response(serializer.data)
