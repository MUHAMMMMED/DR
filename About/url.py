
from django.urls import path
from  About.views  import *


app_name='About'

urlpatterns = [
 path('',about, name="About"),
 
 path('questions',qestionsAndAnswersPage, name="Questions"),
 
 path('ContactUs',ContactUs, name="ContactUs"),

 ] 
 
 


 