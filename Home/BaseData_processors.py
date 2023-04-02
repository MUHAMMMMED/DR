from django.shortcuts import render
from Home.models import *
 
# Create your views here.
def Basegeneric(request):
    information = Information.objects.all()

    #  =.objects.last()  
 
    context = {
    'information': information, }  
  
    return context 
 
 
 
  
 


 
 
    