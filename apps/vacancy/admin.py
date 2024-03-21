from django.contrib import admin

from apps.vacancy.models import Vacancy
# Register your models here.
from modeltranslation.admin import TranslationAdmin

class VacancyAdmins(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('title_ru', 'desc_ru', 'salary')}),
        (u'Ky', {'fields': ('title_ky', 'desc_ky')})
    ]

admin.site.register(Vacancy, VacancyAdmins)