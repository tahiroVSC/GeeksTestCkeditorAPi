from django.urls import path
from apps.TrainZone.views import TrainZoneView


urlpatterns = [
    path('train-zone/', TrainZoneView.as_view(),)
    ]
