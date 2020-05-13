def price_format(value):
    return f'R$ {value:.2f}'.replace('.', ',')

def cart_total_quantity(cart):
    return sum([item['quantity'] for item in cart.values()])

def cart_total_price(cart):
    return sum(
        [
            item.get('summed_sale_price')
            if item.get('summed_sale_price')
            else item.get('summed_price')
            for item
            in cart.values()
        ]
    )
