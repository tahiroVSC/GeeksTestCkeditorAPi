from django.contrib import admin
from django.db import models
from apps.Offering.models import Offering
from .widgets import ImageSelectWidget

from modeltranslation.admin import TranslationAdmin

class OfferingAdmins(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'price','photo')}),
        (u'Ky', {'fields': ('title_ky',)})
    ]


admin.site.register(Offering, OfferingAdmins)