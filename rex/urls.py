from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signup6',views.signup6,name='signup6'),
    path('test',views.signup4,name='signup4')

]
