"""
URL configuration for Triatlon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include 
from django.views.static import serve 
from django.urls import re_path
from Triatlon import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.TrainZone.urls')),
    path('api/v1/', include('apps.Faq.urls')),
    path('api/v1/', include('apps.Services.urls')),
    path('api/v1/', include('apps.Review.urls')),
    path('api/v1/', include('apps.Abonements.urls')),
    path('api/v1/', include('apps.About.urls')),
    path('api/v1/', include('apps.vacancy.urls')),
    path('api/v1/', include('apps.application.urls')),
    path('api/v1/', include('apps.trainer.urls')),
    path('api/v1/', include('apps.contacts.urls')),
    path('api/v1/', include('apps.files.urls')),
    path('api/v1/', include('apps.Offering.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    # drf_spectacular

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
