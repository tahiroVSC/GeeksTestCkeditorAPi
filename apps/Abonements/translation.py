from modeltranslation.translator import translator, TranslationOptions
from apps.Abonements.models import Abonement

class AbonementTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'time', 'price')

translator.register(Abonement, AbonementTranslationOptions)