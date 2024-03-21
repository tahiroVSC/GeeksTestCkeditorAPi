from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.Faq.models import Faq
from modeltranslation.admin import TranslationAdmin

class FaqAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('question_ru', 'answer_ru', )}),
        (u'Ky', {'fields': ('question_ky', 'answer_ky', )})
    ]

admin.site.register(Faq, FaqAdmin)


admin.site.unregister(Group)