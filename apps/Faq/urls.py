from django.urls import path
from apps.Faq.views import FaqAPIViews

urlpatterns = [
    path('faq/', FaqAPIViews.as_view(), name='Faq-list-create'),
]
