from rest_framework import serializers
from apps.Review.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('name', 'jobtitle','description')