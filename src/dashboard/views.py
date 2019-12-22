from django.shortcuts import render,redirect
from . models import Noticeboard
from django.contrib.auth.decorators import login_required

@login_required
def noticeboard(request):
    notices = Noticeboard.objects.all()
    return render(request, 'dashboard/index.html',{'notices':notices})

@login_required
def notice_detail(request, slug):
    notice_body = Noticeboard.objects.get(slug=slug)
    return render(request, 'dashboard/details.html', {'notice_body':notice_body})