 
from django.urls import path
from  LandingPage.views import *
app_name='LandingPage'
urlpatterns = [
  path('',landingpage, name="LandingAll"),  
  path('<str:slug>',landingPageDetails, name="landingPageDetails"),
  
 
 
 ] 

 