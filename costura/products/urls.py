from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path(route='',                              view=views.product_list,     name='list'),
    path(route='categories/',                   view=views.category_list,    name='category_list'),
    path(route='categories/add/',               view=views.category_add,     name='category_add'),
    path(route='categories/update/<slug:slug>/',view=views.category_update,  name='category_update'),
    path(route='categories/<slug:slug>/',       view=views.product_category, name='product_by_category'),
    path(route='add/',                          view=views.product_add,      name='add'),
    path(route='search/',                       view=views.product_search,   name='search_results'),
    path(route='<slug:slug>/',                  view=views.product_detail,   name='detail'),
    path(route='<slug:slug>/delete/',           view=views.product_delete,   name='delete'),
    path(route='<slug:slug>/update/',           view=views.product_update,   name='update'),
]
