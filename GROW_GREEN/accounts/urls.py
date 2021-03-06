from django import views
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('register',views.register, name='register'),  #url for signup
    path('login',views.login, name='login'),  #url for signin
    path('logout',views.logout_user, name='logout'),  #url for logout
    path('dashboard',views.dashboard, name='dashboard'),  #url for logout
    path('about',views.about, name='about'),  #url for logout
    path('contact',views.contact_growgreen, name='contact_growgreen'),  #url for logout
    path('test',views.test_website,name='test_website')
]
