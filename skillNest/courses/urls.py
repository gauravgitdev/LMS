from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse
from courses.views import home, coursepage
from django.conf.urls.static import static
from skillNest import settings

# from skillNest.settings import MEDIA_URL, MEDIA_ROOT



urlpatterns = [
    path('', home , name='home'),
    path('course/<str:slug>', coursepage , name='coursepage'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
