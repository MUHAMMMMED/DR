# from django.db import models
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
 
 # Create your models here.


class AboutDR(models.Model):
      Image = models.FileField(upload_to = "files/images/About/Image/%Y/%m/%d/",blank=True, null=True)
      Title= models.CharField(max_length = 300 , null = True)
      Description= models.CharField(max_length = 300 , null = True)
      Spotlight = models.CharField(max_length = 300 , null = True)
      SpotlightDescription= models.CharField(max_length = 300 , null = True)
      
      def __str__(self):
        return self.Title  

class specifications(models.Model):
      Title= models.CharField(max_length = 300 , null = True)
      Image = models.FileField(upload_to = "files/images/About/Image/%Y/%m/%d/",blank=True, null=True)
      Title1= models.CharField(max_length = 300 , null = True)
      Description1= models.CharField(max_length = 300 , null = True)
      Title2= models.CharField(max_length = 300 , null = True)
      Description2= models.CharField(max_length = 300 , null = True)
      Title3= models.CharField(max_length = 300 , null = True)
      Description3= models.CharField(max_length = 300 , null = True)  
          
      def __str__(self):
        return self.Title 
    
class About(models.Model):
     Ourmessage= models.CharField(max_length = 300 , null = True)  
     Ourvision= models.CharField(max_length = 300 , null = True)  
     rateus= models.CharField(max_length = 300 , null = True)  
     
     def __str__(self):
        return self.Ourmessage  

    
class Reviews(models.Model):
     Image = models.FileField(upload_to = "files/images/About/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     
     def __str__(self):
        return self.Name
    
    
class Clinicphotos(models.Model):
   image = models.FileField(upload_to = "files/images/About/Image/%Y/%m/%d/",blank=True, null=True)
   imagename = models.CharField(max_length = 300 , null = True)
   
   def __str__(self):
        return self.imagename  
    
    
  

class QuestionsAndAnswersPage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = False)
    question= models.CharField(max_length = 300 , null = True)
    answer= RichTextField()
    
    class Meta:
     ordering = ("-created_at",)

    def __str__(self):
        return self.question