from django import template
import math
register = template.Library()

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    else:
        sellprice=price
        sellprice=price - (price * discount / 100)
        return math.ceil(sellprice)
    
@register.filter
def rupee(price):
    return f'₹{price}'    