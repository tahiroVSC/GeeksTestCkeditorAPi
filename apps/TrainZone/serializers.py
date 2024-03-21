from .models import TrainZone
from rest_framework import serializers

class TrainZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainZone
        exclude = ('title','description')


class TrainZoneValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainZone
        fields = '__all__'