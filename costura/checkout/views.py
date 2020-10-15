from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView

from costura.products.models import Product

from .models import Order

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout/checkout.html'
    def post(self,request, *args, **kwargs):
        items   = request.POST.get('items','')
        address = request.POST.get('address',"")
        total   = request.POST.get('total',"")
        obs     = request.POST.get('obs',"")
        order = Order.objects.create_order(items=items, user=request.user, address=address,total=total,obs=obs)
        order.save()
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context_data['order'] = order
        return response
    
checkout_view = CheckoutView.as_view()

def checkout(request):
    order = None
    if request.method == "POST":
        items   = request.POST.get('items','')
        address = request.POST.get('address',"")
        total   = request.POST.get('total',"")
        obs     = request.POST.get('obs',"")
        user    = request.user
        order   = Order(items=items,address=address,user=user,total=total,obs=obs)
        order.save()
        order   = order
        return render(request,'checkout/checkout.html',{'order':order})
    return render(request,'checkout/cart_detail.html',{'order':order})

def complete(request):
    return render(request,'checkout/checkout.html')

class OrdersByUserView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'checkout/orders.html'
    def get_queryset(self):
        order_list = Order.objects.filter(user=self.request.user)
        return order_list
    
orders_by_user = OrdersByUserView.as_view()

"""
class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                user=request.user, cart_items=cart_items
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('checkout:cart_item')
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context_data['order'] = order
        return response

checkout        = CheckoutView.as_view()

class OrdersByUserView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'checkout/orders.html'
    
    def get_queryset(self):
        user_name = self.request.user.username
        order_list = Order.objects.filter(username=user_name)
        return order_list
    
orders_by_user = OrdersByUserView.as_view()
"""
