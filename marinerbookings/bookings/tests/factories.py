from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Guest


class GuestFactory(factory.django.DjangoModelFactory):

    guest_first_name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.guest_first_name))
    guest_last_name = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    booking_source = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Guest.BookingSource.choices]
)
    city = factory.Faker('city')

    class Meta:
        model = Guest
