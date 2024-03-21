from django.contrib import admin

from apps.trainer.models import Trainer, Type_of_trainer
from modeltranslation.admin import TranslationAdmin


class TrainerAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('name_ru', 'photo', 'description_ru', 'type_of_trainer')}),
        (u'Ky', {'fields': ('name_ky', 'description_ky')})
    ]


class Type_of_trainerAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('name_ru',)}),
        (u'Ky', {'fields': ('name_ky',)})
    ]


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Type_of_trainer, Type_of_trainerAdmin)
