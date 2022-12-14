from rest_framework import serializers
from .models import Property
from rest_framework.serializers import IntegerField


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['key', 'value']

    def get_properties(self, data):
        values = {}
        for key, value in data.items():
            values.update({'key': key, 'value': value})
        return super().get_properties(values)


class EntitySerializer(serializers.ModelSerializers):
    value = IntegerField(...)
    properties = PropertySerializer(read_only=True, many=True)

    def get_properties(self, data):
        data['value'] = data['data[value]']
        data.pop('data[value]')
        return super().get_properties(data)
