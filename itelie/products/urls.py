from django.urls import path
from . import views

app_name="products"

urlpatterns= [
    path(route='',              view=views.ProductListView.as_view(), name='list'),
    #path(route='add/', view=views.ProductCreateView.as_view(),name='add'),
    path(route='categories/',   view=views.CategoryListView.as_view(),name='category_list'),
    path(route='categories/<slug:slug>', view=views.ProductCategory.as_view(), name='product_by_category'),
    path(route='search/',       view=views.ProductSearchView.as_view(), name='search_results'),
    path(route='<slug:slug>/',  view=views.ProductDetailView.as_view(), name='detail'),
    #path(route='<slug:slug>/update/',view=views.ProductUpdateView.as_view(),name='update'),
]