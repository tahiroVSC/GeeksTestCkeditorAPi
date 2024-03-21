from django.contrib import admin

from apps.Services.models import Services
from modeltranslation.admin import TranslationAdmin

class ServicesAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'note_ru', 'hours_week_ru', 'price_ru', )}),
        (u'Ky', {'fields': ('title_ky', 'note_ky', 'hours_week_ky', 'price_ky',)})
    ]

admin.site.register(Services, ServicesAdmin)