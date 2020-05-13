from django.template import Library
from utils import utils

register = Library()

@register.filter
def cart_total_quantity(cart):
    return utils.cart_total_quantity(cart)

@register.filter
def cart_total_price(cart):
    return utils.cart_total_price(cart)
