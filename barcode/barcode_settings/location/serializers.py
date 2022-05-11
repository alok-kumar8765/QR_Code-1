from dataclasses import fields
from rest_framework import serializers

class locationserializer(serializers.ModelSerializer):
    pin=serializers.CharField()
    class Meta:
        fields = ['pin']
