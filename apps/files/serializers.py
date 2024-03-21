from .models import File
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ('name', 'file')


class FileValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'