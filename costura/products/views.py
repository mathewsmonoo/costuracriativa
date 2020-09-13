from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Category, Product


#---------------------Category Views-------------------------------
class CategoryDetailView(DetailView):
    model = Category
    paginate_by = 8


class CategoryListView(ListView):
    model       = Category
    paginate_by = 8

#---------------------Product Views-------------------------------
class ProductDetailView(DetailView):
    model = Product
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products:list')
    
class ProductListView(ListView):
    model       = Product
    paginate_by = 8


'''
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields =['name', 'description',]
    action = "Update"'''

#---------------------Linking Views-------------------------------
class ProductCategoryView(ListView):

    template_name   = 'products/product_by_category.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

#----------------------Search View--------------------------------
class ProductSearchView(ListView):
    model           = Product
    template_name   = 'products/search_results.html'
    paginate_by     = 8

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)
            )
        else:
            object_list = self.model.objects.none()
        return object_list

#--------------------------------------------------------------------------------------
category_detail  = CategoryDetailView.as_view()
category_list    = CategoryListView.as_view()
product_detail   = ProductDetailView.as_view()
product_add      = ProductCreateView.as_view()
product_list     = ProductListView.as_view()
product_category = ProductCategoryView.as_view()
product_search   = ProductSearchView.as_view()