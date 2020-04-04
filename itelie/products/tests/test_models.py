import pytest
from ..models import Product
from .factories import ProductFactory, product

#Connects our tests to database
pytestmark = pytest.mark.django_db

def test___str__(product):
    assert product.__str__() == product.name
    assert str(product) == product.name

def test_get_absolute_url(product):
    url = product.get_absolute_url()
    assert url == f'/products/{product.slug}/'

def test_get_profit(product):
    profit = product.get_profit()
    assert profit == (product.price - product.cost)