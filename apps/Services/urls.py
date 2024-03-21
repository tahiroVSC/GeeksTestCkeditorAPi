from django.urls import path
from apps.Services.views import ServicesAPIViews

urlpatterns = [
    path('services/', ServicesAPIViews.as_view(), name='Services-list-create')
]
