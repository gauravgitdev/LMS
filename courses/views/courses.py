from django.shortcuts import render,HttpResponse
from courses.models import Course


def coursepage(request, slug):
    course= Course.objects.get(slug=slug)
    context={
        "course": course,
    }
    return render(request, "courses/course_page.html", context=context)