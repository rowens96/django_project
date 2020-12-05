from django.contrib import admin
from pages.models import Student
from pages.models import Pathway
from pages.models import Course

admin.site.register(Student)
admin.site.register(Pathway)
admin.site.register(Course)