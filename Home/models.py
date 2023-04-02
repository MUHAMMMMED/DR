from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slide(models.Model):
    WebImage = models.FileField(upload_to = "files/images/Home/Slide/Image/%Y/%m/%d/",blank=True, null=True)
    MobilImage = models.FileField(upload_to = "files/images/Home/Slide/Image/%Y/%m/%d/",blank=True, null=True)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Description = models.CharField(max_length = 300  ,blank=True, null=True)
    video_id = models.CharField(max_length = 100 ,blank=True, null=True)
    questionImage=models.FileField(upload_to = "files/images/Home/Slide/Image/%Y/%m/%d/",blank=True, null=True) 
    
    def __str__(self):
         return self.Title

  
class youtubeBeforeAfter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    VideoName = models.CharField(max_length=100,blank=True, null=True)
    video_id = models.CharField(max_length = 300 ,blank=True, null=True)
    
    class Meta:
     ordering = ("-created_at",)
        
    def __str__(self):
         return self.VideoName

class ImageBeforeAfter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Image = models.FileField(upload_to = "files/images/Home/ImageBeforeAfter/Image/%Y/%m/%d/",blank=True, null=True)
    ImageName = models.CharField(max_length=100)
    class Meta:
     ordering = ("-created_at",)
        
    def __str__(self):
         return self.ImageName
     
class Information(models.Model):#   
   LOGO = models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   FaviconIco= models.FileField(upload_to = "files/images/Home/Information/Image/%Y/%m/%d/",blank=True, null=True)
   WebName= models.CharField(max_length = 300 ,blank=True, null=True)
   Copyright = models.CharField(max_length = 300 ,blank=True, null=True)
   PHONE = models.CharField(max_length = 300 ,blank=True, null=True)
   Twitterlinke= models.CharField(max_length=500,blank=True, null=True)
   instagramlinke= models.CharField(max_length=500,blank=True, null=True)
   facebooklinke= models.CharField(max_length=500,blank=True, null=True)
   Youtubelinke= models.CharField(max_length=500,blank=True, null=True)
   linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
   Whatsapp= models.CharField(max_length=500,blank=True, null=True) 
   snapchat= models.CharField(max_length=500,blank=True, null=True) 
   Address= models.CharField(max_length=500,blank=True, null=True)
   OpeningHours= models.CharField(max_length=500,blank=True, null=True)  
   
   def __str__(self):
         return self.Copyright

 
class Questions(models.Model):
    active = models.BooleanField(default = False)
    question= models.CharField(max_length = 500 ,blank=True, null=True)
    answer= RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

