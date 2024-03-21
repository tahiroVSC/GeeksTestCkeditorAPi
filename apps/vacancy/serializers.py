from rest_framework import serializers
from apps.vacancy.models import Vacancy


class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('title','desc')
