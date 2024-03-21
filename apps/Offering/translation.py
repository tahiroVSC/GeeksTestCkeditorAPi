from modeltranslation.translator import translator, TranslationOptions
from apps.Offering.models import Offering

class OfferingTranslationOption(TranslationOptions):
    fields = ('title',)
    
translator.register(Offering, OfferingTranslationOption)