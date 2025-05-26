from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse
from courses.views import home


urlpatterns = [
    path('', home , name='home'),
]
