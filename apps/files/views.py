from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import File
from .serializers import FileSerializer

# Create your views here.

class FileView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer




