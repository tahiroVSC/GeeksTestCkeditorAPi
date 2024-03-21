from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.application.models import Application
# Register your models here.
from modeltranslation.admin import TranslationAdmin


admin.site.register(Application)
# admin.site.unregister(Group)
# admin.site.unregister(User)