from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.About.models import AboutUs
from apps.About.serializers import (
    AboutUsValidatorSerializer, AboutUsSerializer)


class AboutUsViewAPI(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


# class AboutUsDetailViewAPI(RetrieveAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#     lookup_field = 'id'
