#from django.conf.urls import url
from django.urls import path
from accounts import views
#from django.contrib.auth.views import LoginView, LogoutView, register_view
from accounts.views import login_view, register_view, logout_view, view_profile, view_attendance, view_search, view_searchresult
app_name="accounts"

urlpatterns = [
    path('search/',views.view_search, name='search'),
    path('search_results/',views.view_searchresult, name='search_results'),
    path('profile/', views.view_profile, name='profile'),
    path('Attendance/', views.view_attendance, name='attendance'),
    path('grades/', views.view_grades, name='grades'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login')
]
#urlpatterns += staticfiles_urlpatterns()
#if built-in login functions would have been used#path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
#  path('logout/', LogoutView.as_view (template_name= 'accounts/logout.html'), name='logout'),
# path('register/', register_view.as_view (template_name= 'accounts/reg_form.html'), name='register'),