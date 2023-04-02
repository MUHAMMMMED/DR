from django.shortcuts import render
from Stories.models import *

def stories(request):


    Image =ImageStory.objects.filter(active=True)
    youtube =youtubeStory.objects.filter(active=True)
    context = {
        'Image':Image ,
        'youtube':youtube ,
        
      }  
 
    return render(request, 'stories.html', context) 



 