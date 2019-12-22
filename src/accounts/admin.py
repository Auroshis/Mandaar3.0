from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import UserProfile, StudentAttendance, StudentGrades


class UserProfileAdmin(admin.ModelAdmin):#for efficiently displaying the fields in database in admin site
    list_display = ('user', 'student_name', 'cgpa', 'mail', 'phone')#better to be in same order as that of models

#class AttendanceAdmin(admin.ModelAdmin):#for efficiently displaying the fields in database in admin site
 #   list_display = ('user', 'student_name', 'semester', 'subject1', 'attendance1', 'subject1', 'attendance1', 'subject1', 'attendance1', 'subject1', 'attendance1', 'subject1', 'attendance1', 'subject', 'attendance6')#better to be in same order as that of models
    
admin.site.register(StudentAttendance)
admin.site.register(StudentGrades)
admin.site.register(UserProfile,UserProfileAdmin)
