from django.contrib import admin
from django.urls import path
from  Blog.views import *

app_name='Blog'
urlpatterns = [
 
 path('',blog, name="blogAll"),
 
 path('<int:id>/',blogdetails, name="blogdetails"),


 ] 
