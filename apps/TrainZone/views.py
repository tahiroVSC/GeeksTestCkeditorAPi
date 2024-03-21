from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import TrainZone
from .serializers import TrainZoneSerializer

# Create your views here.

class TrainZoneView(ListAPIView):
    queryset = TrainZone.objects.all()
    serializer_class = TrainZoneSerializer



