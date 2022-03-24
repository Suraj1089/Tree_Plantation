from django import views
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('register',views.register, name='register'),  #url for signup
    path('login',views.login, name='login'),  #url for signin
]
