from rest_framework import serializers
from apps.About.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = ('text', 'add_text')



class AboutUsValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=None)
    add_text = serializers.CharField(max_length=None)
