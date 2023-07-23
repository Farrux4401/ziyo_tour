from modeltranslation.translator import translator, TranslationOptions
from .models import Destination, Package


class DestinationTranslationOptions(TranslationOptions):
    fields = ('country', 'desc')


class PackageTranslationOptions(TranslationOptions):
    fields = ('destination', 'title', 'description')


translator.register(Destination, DestinationTranslationOptions)
translator.register(Package, PackageTranslationOptions)
