from django.urls import path
from  Stories.views  import *
 
from django.conf.urls.static import static
from django.conf import settings
app_name='Stories'
 
urlpatterns = [
 path('',stories, name="stories"),
 
 

 ] 
 
 


 