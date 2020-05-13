from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib import messages

from itelie.products.models import Product, Variation


class AddToCart(View):
    def get(self, *args, **kwargs):

        http_referer = self.request.META.get('HTTP_REFERER', reverse('products:list'))

        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(self.request,'Produto não existe')
            return redirect(http_referer)

        variation   = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product     = variation.product

        product_id      = product.id
        product_name    = product.name
        variation_name  = variation.name or ''
        unitary_price   = variation.price
        unitary_sale_price = variation.sale_price
        quantity        = 1
        slug            = product.slug
        #image          = product.image
        
        #messages.error(self.request, f'{product_id}-{product_name}-{variation_name}-{unitary_price}-{unitary_sale_price}-{quantity}-{slug}')
        #return redirect(http_referer)

        if variation.stock < 1 :
            messages.error(self.request, 'Produto sem estoque!')
            return redirect(http_referer)
        
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()
    
        cart = self.request.session['cart']

        if variation_id in cart:
            cart_quantity  =  cart[variation_id]['quantity']
            cart_quantity  += 1

            if variation_stock < cart_quantity:
                messages.warning(self.request,f'Estoque insuficiente para {cart_quantity}x no produto "{product_name}". Adicionamos {variation_stock}x no seu carrinho.')

            #cart_quantity = variation_stock

            cart[variation_id]['quantity']          += cart_quantity
            cart[variation_id]['summed_price']      = str(unitary_price * cart_quantity)
            cart[variation_id]['summed_sale_price'] = str(unitary_sale_price * cart_quantity)

        else:
            cart[variation_id] = {
                'product_id':           product_id,
                'product_name':         product_name,
                'variation_name':       variation_name,
                'variation_id':         variation_id,
                'unitary_price':        str(unitary_price),
                'unitary_sale_price':   str(unitary_sale_price),
                'summed_price':         str(unitary_price),
                'summed_sale_price':    str(unitary_sale_price),
                'quantity':             1,
                'slug':                 slug,
                #'imagem': imagem,
            }

        self.request.session.save()

        messages.success(self.request,f'Produto {product_name} {variation_name} adicionado ao seu carrinho {cart[variation_id]["quantity"]}x.')
        return redirect(http_referer)


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('products:list'))
        variation_id = self.request.GET.get('variation_id')

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            return redirect(http_referer)

        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)
        
        cart = self.request.session['cart'][variation_id]

        messages.success(self.request,f'Produto {cart["product_name"]} {cart["variation_name"]} removido do seu carrinho.')

        del self.request.session['cart'][variation_id]
        self.request.session.save()
        return redirect(http_referer)

class Cart(View):
    def get(self, *args, **kwargs):
        context = {'cart': self.request.session.get('cart', {})}
        return render(self.request, 'cart/cart_detail.html', context)
