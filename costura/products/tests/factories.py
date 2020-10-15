import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from ..models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))

    class Meta:
        model = Category

@pytest.fixture
def category():
    return CategoryFactory()

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    price = factory.fuzzy.FuzzyDecimal(0, 99.9)
    discount_price = factory.fuzzy.FuzzyDecimal(0, 99.9)
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    stock = factory.fuzzy.FuzzyInteger(0, 100)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product

@pytest.fixture
def product():
    return ProductFactory()
