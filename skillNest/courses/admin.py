from django.contrib import admin
from courses.models import Course , Learning , Tag , Prerequisite
from courses.models import Video
# Inline admin to show Tag entries inside the Course admin page
class TagMode(admin.TabularInline):
    model = Tag
# Inline admin to show Prerequisite entries inside the Course admin page
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
# Inline admin to show Learning entries inside the Course admin page
class LearningAdmin(admin.TabularInline):
    model = Learning
# Customize the admin interface for the Course model
class VideoAdmin(admin.TabularInline):
    model = Video
# Main admin for Course, using the inlines above
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagMode, PrerequisiteAdmin, LearningAdmin,VideoAdmin]
# Register the Course model with the customized admin
admin.site.register(Course, CourseAdmin)



admin.site.register(Video)



