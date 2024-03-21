from django.urls import path
from apps.application.views import ApplicationsAPIViews

urlpatterns = [
    path('application/', ApplicationsAPIViews.as_view(),
         name='application-list-create'),
#     path('application/<int:id>/', ApplicatonDetailAPIVeiws.as_view(),
#          name='application-detail'),
]
