from django.db import models

class Course(models.Model):
 name= models.CharField(max_length = 30, null = False)
 description = models.CharField(max_length = 200, null = True)
 price = models.IntegerField(null = False)
 discount = models.IntegerField(null = False, default = 0)
 active = models.BooleanField(default = False)
 thumbnails = models.ImageField(upload_to = "files/thumbnails/")
 date = models.DateTimeField(auto_now_add = True)
 resourse = models.FileField(upload_to = "files/resourses/")
 length = models.IntegerField(null = False)

class CourseProperty(models.Model):
    description = models.CharField(max_length = 30, null = True)
    course = models.ForeignKey(Course , on_delete = models.CASCADE, null= True)

    class Meta :
       abstract = True


class Tag(CourseProperty):
   pass
    

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
   pass
    