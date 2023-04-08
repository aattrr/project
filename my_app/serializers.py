from rest_framework import serializers
from .models import Entity, Property
from django.contrib.auth.models import User


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = serializers.ALL_FIELDS


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = serializers.ALL_FIELDS


class EntitySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(read_only=True, many=True)

    class Meta:
        model = Entity
        fields = ('value', 'properties')
