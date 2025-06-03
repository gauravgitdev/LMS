from django.db import models
from courses.models import Course,UserCourse
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length = 50 , null= False)
    payment_id = models.CharField(max_length= 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"