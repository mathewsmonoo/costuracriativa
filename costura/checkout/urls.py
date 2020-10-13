from django.urls import path
from . import views

app_name="checkout"

urlpatterns=[
    path(route='',         view=views.checkout, name='checkout'),
    path(route='complete', view=views.complete,   name='complete'),
]

"""
urlpatterns=[
    path(route='cart/add/<slug:slug>',view=views.create_cartitem,name='create_cartitem'),
    path(route='cart/',view= views.cart_item,name='cart_item'),
    path('checkout/',  view= views.checkout, name='checkout'),
    path(route='orders/', view= views.orders_by_user, name='ordersbyuser'),
]
"""

