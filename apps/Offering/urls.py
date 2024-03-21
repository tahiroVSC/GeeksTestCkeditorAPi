from django.urls import path

from apps.Offering.views import  OfferingAPIViews

urlpatterns = [
    path('offering/', OfferingAPIViews.as_view(), name='Offering-list-create'),
    # path('offering/<int:pk>/', OfferingDetailViewAPI.as_view(), name='Offering-detail'),
]
