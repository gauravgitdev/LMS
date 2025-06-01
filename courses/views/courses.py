from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from courses.models import Course,Video


def coursepage(request, slug):
    course = get_object_or_404(Course, slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')
    try:
        serial_number = int(serial_number)
        video = Video.objects.get(serial_number=serial_number, course=course)
    except (TypeError, ValueError, Video.DoesNotExist):
        video = Video.objects.filter(course=course).first() 
       
    if((request.user.is_authenticated is False) and (video.ispreview is False)):
        return redirect('login')
    context = {
        "course": course,
        "video": video,
        "videos": videos,
    }
    return render(request, "courses/course_page.html", context)