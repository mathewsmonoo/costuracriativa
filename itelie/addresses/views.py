from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Address


class AddressDetailView(DetailView):
    model = Address

class AddressCreateView(LoginRequiredMixin, CreateView):
    model  = Address
    fields = '__all__'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class AddressListView(LoginRequiredMixin, ListView):
    model = Address

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model  = Address
    fields = '__all__'
    action = "Update"
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

