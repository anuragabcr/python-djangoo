from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.Serializer):
    img1 = serializers.ImageField()
    img2 = serializers.ImageField()
    img3 = serializers.ImageField()
    img4 = serializers.ImageField()

    def create(self, validated_data):
        return Images.objects.create(**validated_data)
