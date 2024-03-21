from django.contrib import admin
from .models import TrainZone
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class TrainZoneAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('photo','title_ru', 'description_ru',)}),
        (u'Ky', {'fields': ('title_ky', 'description_ky', )})
    ]


admin.site.register(TrainZone,TrainZoneAdmin)