from modeltranslation.translator import translator, TranslationOptions
from apps.Review.models import Review

class ReviewTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'jobtitle')

translator.register(Review, ReviewTranslationOptions)