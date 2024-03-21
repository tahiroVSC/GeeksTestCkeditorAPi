from modeltranslation.translator import translator, TranslationOptions
from apps.TrainZone.models import TrainZone

class TrainZoneTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(TrainZone,TrainZoneTranslationOptions)