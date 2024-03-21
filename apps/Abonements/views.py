from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.Abonements.models import Abonement
from apps.Abonements.serializers import (
    AbonementValidatorSerializer, AbonementSerializer)


class AbonementViewAPI(ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer


# class AbonementDetailViewAPI(RetrieveAPIView):
#     queryset = Abonement.objects.all()
#     serializer_class = AbonementSerializer
