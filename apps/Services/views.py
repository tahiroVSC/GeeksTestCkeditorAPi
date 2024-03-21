from rest_framework.generics import ListAPIView
from apps.Services.serializers import ServicesSerializers
from apps.Services.models import Services


class ServicesAPIViews(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
