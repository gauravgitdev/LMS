from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from courses.models import Course,Video,Payment
from django.conf import settings
from time import time
import razorpay
client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
  # Replace with your Razorpay key ID and secret

def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user =None
       
    if (request.user.is_authenticated is False):
        return redirect('login')
    user = request.user    
    action = request.GET.get('action')
    order = None
    payment = None
    if action == "create_payment":
         amount = int(round(( course.price - (course.price * course.discount * 0.01)) * 100 )) # Convert to paise
         currency = 'INR'
         notes = {
             "email": user.email,
             "name":f'{user.first_name} {user.last_name}',
         }
         receipt = f"gaurav-{int(time())}"
         order = client.order.create(
             {
                 "amount": amount,
                 "currency": currency,
                 "receipt": receipt,
                 "notes": notes,
             }
         )
         payment = Payment()
         payment.user = user
         payment.course = course
         payment.order_id = order['id']
         payment.save()
    context = {
        "course": course, 
         "order": order,
         "payment": payment,
         "user": user,
    }
    return render(request, "courses/check_out.html", context)