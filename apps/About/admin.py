from django.contrib import admin
from apps.About.models import AboutUs
from modeltranslation.admin import TranslationAdmin

class AboutUsAdmin(TranslationAdmin):
     fieldsets = [
        (u'Ru', {'fields': ('text_ru', 'add_text_ru')}),
        (u'Ky', {'fields': ('text_ky', 'add_text_ky')})
    ]

admin.site.register(AboutUs, AboutUsAdmin)