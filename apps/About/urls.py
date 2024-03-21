from django.urls import path
from apps.About.views import AboutUsViewAPI


urlpatterns = [
    path('about-us/', AboutUsViewAPI.as_view()),
    # path('about-us/<int:id>/', AboutUsDetailViewAPI.as_view()),
]
