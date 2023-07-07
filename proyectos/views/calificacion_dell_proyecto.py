from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.models import Inscrito, Proyecto, Entrega
from proyectos.serializers.lista_proyectos import *

class ListaDeProyectosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ListaProyectoSerializer

    @action(detail=True, methods=['get'])
    def get_usuario_proyectos(self, request, *args, **kwargs):
        ficha_id = kwargs['ficha_id']

        inscritos = Inscrito.objects.filter(ficha_id=ficha_id)
        integrante_ids = inscritos.values_list('id', flat=True)

        proyectos = Proyecto.objects.filter(aprendiz__id__in=integrante_ids)

        # Cambiar el estado del atributo "calificacion" de los proyectos
        for proyecto in proyectos:
            # Realiza las condiciones y cambios necesarios en el atributo "calificacion"
            if proyecto.estado == 'terminado' or proyecto.estado == 'en desarrollo':
                entregas = Entrega.objects.filter(proyecto=proyecto.id)
                
                # Verificar si todas las entregas tienen la misma calificación
                calificaciones = entregas.values_list('calificacion', flat=True).distinct()
                if len(calificaciones) == 1:
                    calificacion = calificaciones[0]
                    if calificacion == 'aprobado':
                        proyecto.calificacion = 'calificado'
                    elif calificacion == 'en revision':
                        proyecto.calificacion = 'calificar entrega'
                    elif calificacion == 'No aprobado':
                        proyecto.calificacion = 'entrega no aprobada'

                else:
                    proyecto.calificacion = 'calificar entrega'
                
            elif proyecto.estado == 'anulado':
                proyecto.calificacion = 'calificar entrega'
            else:
                proyecto.calificacion = 'calificar proyecto'

            proyecto.save()  # Guardar los cambios en la base de datos

        serializer = self.get_serializer(proyectos, many=True)
        return Response(serializer.data)
