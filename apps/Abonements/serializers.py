from rest_framework import serializers
from apps.Abonements.models import Abonement


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        exclude = ('title','description','time','price',)


class AbonementValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    gruppa = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=None)
    photo = serializers.ImageField(use_url=True, required=False)
    weekdays = serializers.CharField(max_length=150)
    price_month = serializers.CharField(max_length=20)
    price_year = serializers.CharField(max_length=20)
