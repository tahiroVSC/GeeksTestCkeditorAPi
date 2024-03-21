from modeltranslation.translator import translator, TranslationOptions
from apps.files.models import File

class FileTranslationOptions(TranslationOptions):
    fields = ('name', 'file')


translator.register(File, FileTranslationOptions)