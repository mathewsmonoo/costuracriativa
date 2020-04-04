from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)

from .models import Product


class ProductDetailView(DetailView):
    model = Product

'''class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description',]
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)'''

class ProductListView(ListView):
    model = Product

'''
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields =['name', 'description',]
    action = "Update"'''
