from django.urls import path
from . import views

app_name="checkout"

urlpatterns=[
    path(route='',                  view=views.checkout,                name='checkout'),
    path(route='complete',          view=views.complete_view,           name='complete'),
    path(route='userless',          view=views.userless_checkout,       name='userless'),
    path(route='userlesscomplete',  view=views.userless_complete_view,  name='userlesscomplete'),
    path(route='userorders',        view=views.orders_by_user,          name='ordersbyuser'),
    #path(route='complete', view=views.complete,   name='complete'),
]
