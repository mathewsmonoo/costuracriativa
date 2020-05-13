from django.urls import path
from . import views
app_name="cart"

urlpatterns=[
    path(route='add',   view=views.AddToCart.as_view(),name='add'),
    path(route='remove',view=views.RemoveFromCart.as_view(),name='remove'),
    path(route='',      view=views.Cart.as_view(),name='cart'),
]