from django.urls import path
from . import views

app_name="checkout"

urlpatterns=[
    path(route='',                  view=views.checkout,        name='checkout'),
    path(route='complete',          view=views.complete_view,   name='complete'),
    path(route='userorders',        view=views.orders_by_user,  name='ordersbyuser'),
    path(route='userless',          view=views.userless,        name='userless'),
    #path(route='complete', view=views.complete,   name='complete'),
]
