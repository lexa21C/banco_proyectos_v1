from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from proyectos.views.funciones import *
from django.http import Http404  # Importar la excepción Http404

class AgregarInscritosViewSet(viewsets.ModelViewSet):
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_inscritos(self, request, *args, **kwargs):
        """
        Obtiene la lista de inscritos activos que no pertenecen a ningún grupo, están asociados
        a la misma ficha que un perfil específico y tienen el rol de 'aprendiz'.
        
        Args:
            request (HttpRequest): La solicitud HTTP recibida.
            *args: Argumentos adicionales.
            **kwargs: Argumentos de palabras clave adicionales.

        Returns:
            Response: Una respuesta HTTP con los datos de los inscritos.

        Raises:
            Http404: Si no se encuentra el perfil correspondiente.
        """
        try:
            user_id = kwargs['id_user']
            perfil_id = perfil_conectado(user_id)
            inscritos = Inscrito.objects.select_related('rol').filter(
                perfil_id=perfil_id,
                estado='activo',
                nombre_grupo__isnull=True,
                rol__nombre='aprendiz'
            )
            fichas = inscritos.values('ficha').distinct()
            inscritos_misma_ficha = Inscrito.objects.select_related('rol').filter(
                ficha__in=fichas,
                estado='activo',
                nombre_grupo__isnull=True,
                rol__nombre='aprendiz'
            )
            serializer = self.get_serializer(inscritos_misma_ficha, many=True)
            return Response(serializer.data)
        except Http404:
            return Response("Perfil no encontrado.", status=status.HTTP_404_NOT_FOUND)
