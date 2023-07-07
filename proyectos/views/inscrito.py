from rest_framework import viewsets
from rest_framework.response import Response
from proyectos.models import Inscrito, Ficha
from proyectos.serializers.inscritos import InscritoSerializer


class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

    def create(self, request, *args, **kwargs):
        # Obtener los datos del request
        data = request.data

        # Verificar si el perfil ya está asociado a una ficha en particular
        perfil_id = data.get('perfil')
        ficha_id = data.get('ficha')
        estado = data.get('estado')

        if perfil_id and ficha_id:
            # Verificar si el perfil ya está asociado a una ficha
            exists_inscrito = Inscrito.objects.filter(perfil=perfil_id, ficha=ficha_id).exists()
            if exists_inscrito:
                return Response({'error': 'El perfil ya está asociado a esta ficha'}, status=400)

            # Verificar si el perfil tiene un inscrito con estado activo
            exists_active_inscrito = Inscrito.objects.filter(perfil=perfil_id, estado='activo').exists()
            if exists_active_inscrito:
                return Response({'error': 'El perfil tiene un inscrito con estado activo'}, status=400)

            # Verificar si el estado es inactivo
            if estado != 'inactivo':
                return Response({'error': 'El estado del inscrito debe ser inactivo'}, status=400)

        return super().create(request, *args, **kwargs)
