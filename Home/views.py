from django.shortcuts import render
from Home.models import *
from About.models import *
from LandingPage.models import *
 
# Create your views here.
 

def Homepage(request):
    slide = Slide.objects.all()
    youtube = youtubeBeforeAfter.objects.all()
    Image=ImageBeforeAfter.objects.all()
    questions = Questions.objects.filter(active=True)
    
    aboutDR = AboutDR.objects.all()
    Specifications = specifications.objects.all()   
    about = About.objects.all()  
    reviews = Reviews.objects.all() 
    clinicphotos = Clinicphotos.objects.all()
    
    Landing =LandingPage.objects.filter(active=True)
    
    context = {  
               
     'slide':slide,
     'youtube':youtube,    
     'Image':Image,   
     'questions':questions,
     
     'aboutDR': aboutDR,    
     'Specifications': Specifications  ,    
     'about': about   ,    
     'reviews': reviews,
     'clinicphotos': clinicphotos,
     
     'Landing':Landing,
     
   }

    return render(request, 'home.html', context) 
    


 
 