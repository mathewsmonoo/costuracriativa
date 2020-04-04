from django.template.defaultfilters import slugify

import factory
import factory.fuzzy
import pytest

from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    name  = factory.fuzzy.FuzzyText()
    color = factory.fuzzy.FuzzyText()
    cost = factory.fuzzy.FuzzyDecimal(0.1,99.9)
    price = factory.fuzzy.FuzzyDecimal(0,99.9)
    inventory =  factory.fuzzy.FuzzyInteger(0,100)
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    weight = factory.fuzzy.FuzzyDecimal(0,99.9)
    status = factory.fuzzy.FuzzyInteger(0,1)
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))

    class Meta:
        model = Product

@pytest.fixture
def product():
    return ProductFactory()
