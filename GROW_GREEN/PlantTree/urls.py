from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('navbar', views.navbar, name='navbar'),
    path('footer', views.footer, name='footer'),
    path('test',views.test, name='test'),
    path('plant_ui',views.plant_ui, name='plant_ui'),
    path('plant_tree',views.plant_tree, name='plant_tree'),
    
    
    
]