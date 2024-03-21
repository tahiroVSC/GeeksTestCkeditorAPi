from django.contrib import admin
from .models import File
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class FileAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('file_ru','name_ru',)}),
        (u'Ky', {'fields': ('file_ky', 'name_ky',)})
    ]


admin.site.register(File, FileAdmin)