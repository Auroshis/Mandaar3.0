from django.db import models
from django.contrib.auth.models import User

class StudentAttendance(models.Model):
    user = models.ForeignKey(User,related_name='StudentAttendance',null=True, blank=True, on_delete=models.SET_NULL)#rollno to be used as a primary key
    
    subject1 = models.CharField(max_length=150,default='')
    total_classes1 = models.IntegerField(default= 0)
    classes_attended1 = models.IntegerField(default= 0)
    
    subject2 = models.CharField(max_length=150,default='')
    total_classes2 = models.IntegerField(default= 0)
    classes_attended2 = models.IntegerField(default= 0)
    
    subject3 = models.CharField(max_length=150,default='')
    total_classes3 = models.IntegerField(default= 0)
    classes_attended3 = models.IntegerField(default= 0)
    
    subject4 = models.CharField(max_length=150,default='')
    total_classes4 = models.IntegerField(default= 0)
    classes_attended4 = models.IntegerField(default= 0)
    
    subject5 = models.CharField(max_length=150,default='')
    total_classes5 = models.IntegerField(default= 0)
    classes_attended5 = models.IntegerField(default= 0)
    
    subject6 = models.CharField(max_length=150,default='')
    total_classes6 = models.IntegerField(default= 0)
    classes_attended6 = models.IntegerField(default= 0)

class StudentGrades(models.Model):
    user = models.ForeignKey(User,related_name='StudentGrades',null=True, blank=True, on_delete=models.SET_NULL)#rollno to be used as a primary key
    
    subject1 = models.CharField(max_length=150,default='')
    internal1 = models.IntegerField(default= 0)
    final1 = models.IntegerField(default= 0)
    
    subject2 = models.CharField(max_length=150,default='')
    internal2 = models.IntegerField(default= 0)
    final2 = models.IntegerField(default= 0)
    
    subject3 = models.CharField(max_length=150,default='')
    internal3 = models.IntegerField(default= 0)
    final3 = models.IntegerField(default= 0)
    
    subject4 = models.CharField(max_length=150,default='')
    internal4 = models.IntegerField(default= 0)
    final4 = models.IntegerField(default= 0)
    
    subject5 = models.CharField(max_length=150,default='')
    internal5 = models.IntegerField(default= 0)
    final5 = models.IntegerField(default= 0)
    
    subject6 = models.CharField(max_length=150,default='')
    internal6 = models.IntegerField(default= 0)
    final6 = models.IntegerField(default= 0)

class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True, related_name='UserProfile', blank=True, on_delete=models.SET_NULL)#rollno to be used as a primary key
    student_name = models.CharField(max_length=150,default='')
    branch = models.CharField(max_length=150,default='')
    cgpa = models.FloatField(default=0.0)
    mail = models.EmailField(max_length=254,default='')
    phone = models.CharField(max_length=10,default=0)
    #image = models.ImageField(upload_to='profile_image', blank=True)
    #cv in pdf will be added later on