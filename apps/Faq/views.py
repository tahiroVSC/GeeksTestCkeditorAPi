from rest_framework.generics import ListAPIView
from apps.Faq.serializers import FaqSerializers
from apps.Faq.models import Faq


class FaqAPIViews(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializers
