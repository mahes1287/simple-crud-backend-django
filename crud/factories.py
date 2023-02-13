import factory

from .models import Translation


class TranslationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Translation

    input = factory.Faker("sentence")
    output = factory.Faker("sentence")
    fromUser = factory.Faker("name")
