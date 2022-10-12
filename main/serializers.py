from rest_framework import serializers

from .models import url

class urlSerializer(serializers.Serializer):
    url = serializers.URLField()