from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.vacancy.serializers import VacancySerializers
from apps.vacancy.models import Vacancy


class VacansyAPIViews(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers


class VacansyDetailAPIVeiws(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers
    lookup_field = 'id'
