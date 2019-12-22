'''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required#decorator used to check if the user is logged in or not
from django.contrib.auth.models import User #User model has to be imported in django.

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)#pk  is the primary key of the user in the db.
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)'''

#custom login and registration.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, StudentAttendance, StudentGrades
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm
uniqueid=0

def login_view(request):
    global uniqueid
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid(): 
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #print(user.id)
        uniqueid=user.id
        #print('inside login',uniqueid)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('dashboard:noticeboard')

    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('accounts:login')

    context = {
        'form': form,
    }
    return render(request, "accounts/reg_form.html", context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def view_profile(request):
    #print('this is the unique_id',uniqueid)
    userprofile = UserProfile.objects.get(user_id = uniqueid)
    args = {'userprofile':userprofile}
    return render(request, 'accounts/profile.html', args)
    
def view_attendance(request):
    attendance_details = StudentAttendance.objects.get(user_id = uniqueid)
    attn_sub1=(attendance_details.classes_attended1/attendance_details.total_classes1)*100
    sub1= attendance_details.subject1
    attn_sub2=(attendance_details.classes_attended2/attendance_details.total_classes2)*100
    sub2= attendance_details.subject2
    attn_sub3=(attendance_details.classes_attended3/attendance_details.total_classes3)*100
    sub3= attendance_details.subject3
    attn_sub4=(attendance_details.classes_attended4/attendance_details.total_classes4)*100
    sub4= attendance_details.subject4
    attn_sub5=(attendance_details.classes_attended5/attendance_details.total_classes5)*100
    sub5= attendance_details.subject1
    attn_sub6=(attendance_details.classes_attended6/attendance_details.total_classes6)*100
    sub6= attendance_details.subject6

    context = {
        'attn_sub1':attn_sub1,
        'sub1':sub1,
        'attn_sub2':attn_sub2,
        'sub2':sub2,
        'attn_sub3':attn_sub3,
        'sub3':sub3,
        'attn_sub4':attn_sub4,
        'sub4':sub4,
        'attn_sub5':attn_sub5,
        'sub5':sub5,
        'attn_sub6':attn_sub6,
        'sub6':sub6
    }

    return render(request, 'accounts/attendance.html', context)

def view_grades(request):
    grade_details = StudentGrades.objects.get(user_id=uniqueid)

    sub1 = grade_details.subject1
    internal1 = grade_details.internal1
    final1 = grade_details.final1

    sub2 = grade_details.subject2
    internal2 = grade_details.internal2
    final2 = grade_details.final2

    sub3 = grade_details.subject3
    internal3 = grade_details.internal3
    final3 = grade_details.final3

    sub4 = grade_details.subject4
    internal4 = grade_details.internal4
    final4 = grade_details.final4

    sub5 = grade_details.subject5
    internal5 = grade_details.internal5
    final5 = grade_details.final5

    sub6 = grade_details.subject6
    internal6 = grade_details.internal6
    final6 = grade_details.final6

    marks = {
        'sub1':sub1,
        'internal1': internal1,
        'final1': final1,
        'sub2':sub2,
        'internal2': internal2,
        'final2': final2,
        'sub3':sub3,
        'internal3': internal3,
        'final3': final3,
        'sub4':sub4,
        'internal4': internal4,
        'final4': final4,
        'sub5':sub5,
        'internal5': internal5,
        'final5': final5,
        'sub6':sub6,
        'internal6': internal6,
        'final6': final6,
    }

    return render(request, 'accounts/grades.html', marks)

