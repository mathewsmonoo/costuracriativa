from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Category, Product

#---------------------Category Views-------------------------------
class CategoryDetailView(DetailView):
    model = Category

class CategoryListView(ListView):
    model       = Category
    paginate_by = 8

#---------------------Product Views-------------------------------
class ProductDetailView(DetailView):
    model = Product

'''class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description',]
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)'''

class ProductListView(ListView):
    model       = Product
    paginate_by = 8
    #context_object_name='products'

'''
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields =['name', 'description',]
    action = "Update"'''

#---------------------Linking Views-------------------------------
class ProductCategory(ListView):
    model           = Product
    template_name   = 'products/product_by_category.html'
    paginate_by     = 8

    def get_context_data(self, **kwargs):
        context = super(ProductCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)


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