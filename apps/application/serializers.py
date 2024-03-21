from rest_framework import serializers
from apps.application.models import Application


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
