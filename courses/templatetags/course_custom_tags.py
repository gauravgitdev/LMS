from django import template
import math
from courses.models import UserCourse,Course
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

@register.simple_tag
def is_enrolled(request, course):
    user = None
    is_enrolled = False
    if not request.user.is_authenticated:
        return is_enrolled
    user = request.user
    try:
        user_course = user.usercourse_set.get(user = user,course=course)
        return True
    except:
        return False