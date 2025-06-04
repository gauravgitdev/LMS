from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from courses.models import Course,Video,Payment,UserCourse
from django.conf import settings
from time import time
from django.views.decorators.csrf import csrf_exempt
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
    error = None
    if action == "create_payment":
        try:
            user_course = UserCourse.objects.get(user=user, course=course)
            error = "You have already purchased this course."
        except :
            pass
         
        if error is None:  
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
         "error": error,
    }
    return render(request, "courses/check_out.html", context)

@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id'] #data.get('razorpay_order_id') i can also use this but i am using dictionary style because it will throw exception if key is not present 
            razorpay_payment_id = data['razorpay_payment_id']
            payment = get_object_or_404(Payment, order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user = payment.user, course=payment.course)
            userCourse.save()

            payment.user_course = userCourse
            payment.save()
            return render(request, "courses/my_course.html", {"data": data})
        except:
            return HttpResponse("Payment verification failed", status=400)

     