from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Address

address_fields = [
        "receiver_name",
        "receiver_phone",
        "nickname",
        "address_type",
        "state",
        "city",
        "neighborhood",
        "street",
        "number",
        "extra_data",
    ]


class LimitAccessMixin:     #Created in order to return only adresses from the logged user
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owned_by=self.request.user)

class AddressDetailView(LimitAccessMixin, DetailView):
    model = Address

class AddressCreateView(LoginRequiredMixin, CreateView):
    model  = Address
    fields = address_fields
    success_url = reverse_lazy('addresses:list')
    action = "Adicionar"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.owned_by = self.request.user
        return super(AddressCreateView, self).form_valid(form)

class AddressListView(LimitAccessMixin, LoginRequiredMixin, ListView):
    model = Address

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model  = Address
    fields = address_fields
    success_url = reverse_lazy('addresses:list')
    action = "Atualizar"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.owned_by = self.request.user
        return super(AddressUpdateView, self).form_valid(form)
    
    