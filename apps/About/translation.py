from modeltranslation.translator import translator, TranslationOptions
from apps.About.models import AboutUs

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('text', 'add_text')

translator.register(AboutUs, AboutUsTranslationOptions)