from django.contrib import admin
from apps.contacts.models import Contact
from modeltranslation.admin import TranslationAdmin


class ContactAdmin(TranslationAdmin):
    fieldsets = [
        (u'Ru', {'fields': ('first_number', 'second_number', 'email', 'work_time_ru', 'holiday_work_time_ru', 'address_ru', 'link')}),
        (u'Ky', {'fields': ('work_time_ky', 'holiday_work_time_ky', 'address_ky')})
    ]


admin.site.register(Contact, ContactAdmin)
