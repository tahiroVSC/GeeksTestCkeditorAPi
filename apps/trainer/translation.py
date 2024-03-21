from modeltranslation.translator import translator, TranslationOptions

from apps.trainer.models import Trainer, Type_of_trainer


class TrainerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class Type_of_trainerTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Trainer, TrainerTranslationOptions)
translator.register(Type_of_trainer, Type_of_trainerTranslationOptions)
