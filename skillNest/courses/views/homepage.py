from django.contrib import admin
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("home page")