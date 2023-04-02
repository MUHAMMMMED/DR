from django.shortcuts import render, redirect
from About.models import *
from About.forms import *
# # Create your views here.



def about(request):

    aboutDR = AboutDR.objects.all()
    Specifications = specifications.objects.all()   
    about = About.objects.all()  
    reviews = Reviews.objects.all() 
    clinicphotos = Clinicphotos.objects.all()
 
 
    context = {
    'aboutDR': aboutDR,    
    'Specifications': Specifications  ,    
    'about': about   ,    
    'reviews': reviews,
    'clinicphotos': clinicphotos
    }    
    return render(request, 'About.html', context)
  
   
  
def qestionsAndAnswersPage(request):
    
    Question = QuestionsAndAnswersPage.objects.filter(active=True)

    context = { 'Question': Question }   
    
    return render(request, 'questions.html', context)
 
  
def ContactUs(request):
 
    if request.method=='POST':
        form= booking(request.POST)
        if form.is_valid():
            form.save()

            print('DOne')  
 
            return  redirect ('Landingpage:LandingAll') 
    else:
        form = booking()
        print('404')  
 
    context = { 'form':form, } 
   
    return render(request, 'ContactUs.html', context)