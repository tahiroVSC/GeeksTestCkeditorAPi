from django.urls import path
from apps.Abonements.views import AbonementViewAPI


urlpatterns = [
    path('abonements/', AbonementViewAPI.as_view()),
    # path('abonements/<int:id>/', AbonementDetailViewAPI.as_view()),
]
