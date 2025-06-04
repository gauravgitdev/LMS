from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse
from courses.views import home, coursepage,SignupView,Loginview,signout,checkout, verifyPayment
from django.conf.urls.static import static
from skillNest import settings
from django.conf import settings
# from skillNest.settings import MEDIA_URL, MEDIA_ROOT



urlpatterns = [
    path('', home , name='home'),
    path('logout', signout , name='logout'),
    path('course/<str:slug>', coursepage , name='coursepage'),
    path('check-out/<str:slug>', checkout , name='checkpage'),
    path('verify_payment', verifyPayment , name='verify_payment'),
    path('signup', SignupView.as_view() , name='signup'),
    path('login', Loginview.as_view() , name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)