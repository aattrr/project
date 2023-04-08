from collections import OrderedDict

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import EntitySerializer
from .models import Entity


class EntityViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Просмотр и добавление экземпляров Entity
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        fixed_data = []
        for item in serializer.data:
            single_entity = OrderedDict()
            single_entity['value'] = item['value']
            single_entity['properties'] = {}
            for property in item['properties']:
                single_entity['properties'][property['key']] = property['value']
            fixed_data.append(single_entity)
        return Response(fixed_data)
