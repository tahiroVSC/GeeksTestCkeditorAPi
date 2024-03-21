from django.urls import path
from apps.contacts.views import ContactAPIView, ContactRetrieveAPIView

urlpatterns = [
    path('contacts/', ContactAPIView.as_view()),
    path('contacts/<int:id>/', ContactRetrieveAPIView.as_view()),
]
