from django.urls import path
from apps.vacancy.views import VacansyAPIViews, VacansyDetailAPIVeiws

urlpatterns = [
    path('vacancy/', VacansyAPIViews.as_view(), name='vacancy-list-create'),
    path('vacancy/<int:id>/', VacansyDetailAPIVeiws.as_view(), name='vacancy-detail'),
]
