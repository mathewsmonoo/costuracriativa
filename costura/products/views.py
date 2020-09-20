from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView, FormView
from .models import Category, Product
from .forms import ProductForm, CrispyProductForm
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_admin:
            return True
        else:
            return False

#---------------------Category Views-------------------------------
class CategoryDetailView(DetailView):
    model = Category
    paginate_by = 8

class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    fields = [
        'name','image'
    ]
    action = "Adicionar"

    success_url = reverse_lazy('products:category_list')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, ("Categoria Adicionada com Sucesso!")
        )
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class CategoryListView(ListView):
    model       = Category
    paginate_by = 8

class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    model = Category
    fields = [
        'name','image'
    ]
    action = "Atualizar"
    
    def get_success_url(self):
        return reverse_lazy('products:category_list')
    
    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, ("Categoria Atualizada com Sucesso!")
        )
        form.instance.creator = self.request.user
        form.instance.owned_by = self.request.user
        return super(CategoryUpdateView, self).form_valid(form)


#---------------------Product Views-------------------------------
class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(StaffRequiredMixin, CreateView):
    model = Product
    form_class = CrispyProductForm
    helper = None
    action = "add"
    
    def __init__(self, *args, **kwargs):
        super(ProductCreateView, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'url_action_call'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['helper'] = self.helper
        return context
    
    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, ("Produto Criado com Sucesso!")
        )
        product = form.save()
        return super(ProductCreateView, self).form_valid(form)

class ProductDeleteView(StaffRequiredMixin, DeleteView):
    model = Product

    def get_success_url(self):
        messages.add_message(
            self.request, messages.INFO, ("Produto Deletado com Sucesso.")
        )
        return reverse_lazy('products:list')
    
class ProductListView(ListView):
    model       = Product
    paginate_by = 9

class ProductUpdateView(StaffRequiredMixin, UpdateView):
    model = Product
    form_class = CrispyProductForm
    helper = None
    action = "update"
    
    def __init__(self, *args, **kwargs):
        super(ProductUpdateView, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'url_action_call'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['helper'] = self.helper
        return context
    
    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, ("Produto Aualizado com Sucesso!")
        )
        product = form.save()
        return super(ProductUpdateView, self).form_valid(form)

"""
class ProductUpdateView(StaffRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    action = "update"
    
    def get_success_url(self):
        return reverse('products:detail',kwargs={'slug':self.kwargs['slug']})
    
    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, ("Produto Aualizado com Sucesso!")
        )
        form.instance.creator = self.request.user
        form.instance.owned_by = self.request.user
        return super(ProductUpdateView, self).form_valid(form)
"""

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
category_detail     = CategoryDetailView.as_view()
category_add        = CategoryCreateView.as_view()
category_list       = CategoryListView.as_view()
category_update     = CategoryUpdateView.as_view()
product_add         = ProductCreateView.as_view()
product_detail      = ProductDetailView.as_view()
product_list        = ProductListView.as_view()
product_update      = ProductUpdateView.as_view()
product_category    = ProductCategoryView.as_view()
product_search      = ProductSearchView.as_view()
product_delete      = ProductDeleteView.as_view()
