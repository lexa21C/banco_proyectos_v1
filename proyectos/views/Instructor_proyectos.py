# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from proyectos.models import Inscrito, Proyecto
# from proyectos.serializers.proyecto import ProyectoSerializer

# class ProyectosViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Proyecto.objects.all()
#     serializer_class = ProyectoSerializer

#     @action(detail=True, methods=['get'])
#     def get_usuario_proyectos(self, request, *args, **kwargs):
#         ficha_id = kwargs['ficha_id']

#         inscritos = Inscrito.objects.filter(ficha_id=ficha_id)
#         integrante_ids = inscritos.values_list('id', flat=True)

#         proyectos = Proyecto.objects.filter(aprendiz__id__in=integrante_ids)

#         serializer = self.get_serializer(proyectos, many=True)
#         return Response(serializer.data)



