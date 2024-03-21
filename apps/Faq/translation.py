from modeltranslation.translator import translator, TranslationOptions
from apps.Faq.models import Faq

class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

translator.register(Faq, FaqTranslationOptions)
