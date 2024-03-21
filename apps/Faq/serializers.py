from rest_framework import serializers
from apps.Faq.models import Faq


class FaqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faq
        exclude = ('question', 'answer')


