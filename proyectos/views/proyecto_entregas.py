from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from proyectos.serializers.lista_entregas import ListaEntregaSerializer
from proyectos.models import Entrega
class ProyectoEntregaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entrega.objects.all()
    serializer_class = ListaEntregaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_entregas_por_proyecto(self, request, *args, **kwargs):
        """
        Obtiene las entregas asociadas a un proyecto específico.

        Args:
            request (HttpRequest): La solicitud HTTP recibida.
            *args: Argumentos adicionales.
            **kwargs: Argumentos de palabras clave adicionales.

        Returns:
            Response: Una respuesta HTTP con los datos de las entregas asociadas al proyecto.

        Raises:
            Http404: Si no se encuentra el proyecto correspondiente.
        """
        id_proyecto = kwargs['id_proyecto']
        proyecto = get_object_or_404(Proyecto, id=id_proyecto)
        entregas = Entrega.objects.filter(proyecto=proyecto)
        serializer = ListaEntregaSerializer(entregas, many=True)
        return Response(serializer.data)
