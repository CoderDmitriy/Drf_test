from rest_framework import serializers
from .models import Entity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

    modified_by = serializers.ReadOnlyField(source='modified_by.username')
    value = serializers.ReadOnlyField()
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj):
        values = {}
        for prop in obj.properties.all():
            values[prop.key] = prop.value
        return values
