from modeltranslation.translator import translator, TranslationOptions
from apps.contacts.models import Contact


class ContactTranslationOptions(TranslationOptions):
    fields = ('work_time', 'holiday_work_time', 'address')


translator.register(Contact, ContactTranslationOptions)
