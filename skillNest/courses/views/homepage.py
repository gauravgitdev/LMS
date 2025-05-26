from django.contrib import admin
from courses.models import Course
from django.shortcuts import HttpResponse,render

def home(request):
    courses = Course.objects.all()
    return render(request, "courses/home.html" , context={"courses": courses})
