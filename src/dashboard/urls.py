from django.urls import path
from .import views 
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="dashboard"

urlpatterns = [
    path('', views.noticeboard, name='noticeboard'),
    path('<slug:slug>/', views.notice_detail, name='notice_detail')
]

urlpatterns += staticfiles_urlpatterns()