from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class UserCourse(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE, null= False)
    course = models.ForeignKey(Course , on_delete = models.CASCADE, null= False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User.username} - {self.course.name}"