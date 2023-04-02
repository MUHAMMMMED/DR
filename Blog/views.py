from django.shortcuts import render
from Blog.models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.

def blog(request):

    bloG=Blog.objects.all()
 
    context = { 'bloG':bloG  }  
 
    return render(request, 'blog.html', context) 




def blogdetails(request,id):
 
    Blogdetails= get_object_or_404(Blog,id=id)
    
    context = {     'Blogdetails':Blogdetails   } 

    return render(request, 'blogdetails.html', context)


 