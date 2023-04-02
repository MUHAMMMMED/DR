 
from django.urls import path
from  Home.views  import *
 
app_name='Home'
 
urlpatterns = [
 path('',Homepage, name="Homepage"),

 ] 
 
 


 