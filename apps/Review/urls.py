from django.urls import path
from apps.Review.views import ReviewAPIViews

urlpatterns = [
    path('review/', ReviewAPIViews.as_view(), name='Review-list-create'),
]
