from rest_framework.generics import ListAPIView
from apps.Review.serializers import ReviewSerializers
from apps.Review.models import Review


class ReviewAPIViews(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
