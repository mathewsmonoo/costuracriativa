#The idea is to create a code that will be executed in every view.
from costura.checkout.models import CartItem

def cart_item_middleware(get_response):
    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key: #In some way the session modified the session key
            CartItem.objects.filter(cart_key=session_key).update(
                cart_key=request.session.session_key #Items will be kept after login
            )
        return response
    return middleware

# coding=utf-8

