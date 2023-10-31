from django import template

register = template.Library()


@register.filter(name='is_in_cart')

def is_in_cart(menuitem, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == menuitem.id:
            return True
    return False


@register.filter(name='cart_quantity')

def cart_quantity(menuitem, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == menuitem.id:
            return cart.get(id) 
    return 0


@register.filter(name='price_total')
def price_total(menuitem, cart):
    totalprice = menuitem.price * cart_quantity(menuitem, cart)
    return totalprice



@register.filter(name='total_cart_price')
def total_cart_price(menuitems , cart):
    sum = 0 
    for p in menuitems:
        sum += price_total(p , cart)

    return sum