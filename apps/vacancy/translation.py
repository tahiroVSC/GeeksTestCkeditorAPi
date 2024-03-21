from modeltranslation.translator import translator, TranslationOptions

from apps.vacancy.models import Vacancy

class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)
    
translator.register(Vacancy, VacancyTranslationOptions)
