from rest_framework import viewsets, permissions
from .models import Entity
from .serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        value = self.request.data.get('data[value]')
        if not isinstance(value, int):
            value = None
        serializer.save(
            modified_by=self.request.user,
            value=value
        )
