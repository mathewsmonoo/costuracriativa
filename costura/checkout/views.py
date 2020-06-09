from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView

from costura.checkout.models import CartItem
from costura.products.models import Product


#Adicionar via get; Adicionar produto no carrinho de compras e redireciona para pag do carrinho

class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return reverse('checkout:cart_item')


class CartItemView(TemplateView):

    template_name = 'checkout/cart_detail.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)




# class CreateCartItemView(RedirectView):

#     def get_redirect_url(self, *args, **kwargs):
#         product = get_object_or_404(Product, slug=self.kwargs['slug'])
#         if self.request.session.session_key is None:
#             self.request.session.save()
#         cart_item, created   = CartItem.objects.add_item(self.request.session.session_key, product)

#         if created:
#             messages.success(self.request, 'Produto adicionado com sucesso')
#         else:
#             messages.success(self.request, 'Produto atualizado com sucesso')
#         return reverse('checkout:cart_item')

# class CartItemView(TemplateView):

#     template_name = 'checkout/cart_detail.html'

#     def get_formset(self, clear=False):
#         CartItemFormSet = modelformset_factory(
#             CartItem, fields=('quantity',), can_delete=True, extra=0
#         )
#         session_key = self.request.session.session_key
#         if session_key:
#             if clear:
#                 formset = CartItemFormSet(
#                     queryset=CartItem.objects.filter(cart_key=session_key)
#                 )
#             else:
#                 formset = CartItemFormSet(
#                     queryset=CartItem.objects.filter(cart_key=session_key),
#                     data=self.request.POST or None
#                 )
#         else:
#             formset = CartItemFormSet(queryset=CartItem.objects.none())
#         return formset

#     def get_context_data(self, **kwargs):
#         context = super(CartItemView, self).get_context_data(**kwargs)
#         context['formset'] = self.get_formset()
#         return context

#     def post(self, request, *args, **kwargs):
#         formset = self.get_formset()
#         context = self.get_context_data(**kwargs)
#         if formset.is_valid():
#             formset.save()
#             messages.success(request, 'Carrinho atualizado com sucesso')
#             context['formset'] = self.get_formset(clear=True)
#         return self.render_to_response(context)

create_cartitem = CreateCartItemView.as_view()
cart_item       = CartItemView.as_view()
