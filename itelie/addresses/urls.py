from django.urls import path
from . import views

app_name= "addresses"

urlpatterns= [
    path(route='', view=views.AddressListView.as_view(), name='list'),
    path(route='add/', view=views.AddressCreateView.as_view(),name='add'),
    path(route='<int:pk>/', view=views.AddressDetailView.as_view(), name='detail'),
    path(route='<int:pk>/update/',view=views.AddressUpdateView.as_view(),name='update'),
]