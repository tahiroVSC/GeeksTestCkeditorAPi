from django.urls import path
from apps.trainer.views import TrainerViewAPI, TrainerDetailViewAPI

urlpatterns = [
    path('trainer/', TrainerViewAPI.as_view()),
    path('trainer/<int:id>/', TrainerDetailViewAPI.as_view()),
]
