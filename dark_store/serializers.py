from rest_framework import serializers
from .models import Location, Shelf


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'location', 'identifier', 'weight_capacity', 'created_at']


class LocationSerializer(serializers.ModelSerializer):
    shelves = ShelfSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'is_active', 'created_at', 'shelves']
