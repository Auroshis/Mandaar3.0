from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from Hibiscus30 import views
from django.conf import settings
from django.conf.urls.static import static


#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('dashboard/', include('dashboard.urls'), name='dashboard')
]
