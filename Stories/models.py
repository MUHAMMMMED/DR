from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class youtubeStory(models.Model):
    active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    video_id = models.CharField(max_length = 300 ,blank=True, null=True)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Description= RichTextField(blank=True, null=True)
    class Meta:
     ordering = ("-created_at",)

    def __str__(self):
         return self.Title

class ImageStory(models.Model):
    active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    Image = models.FileField(upload_to = "files/images/Story/Image/%Y/%m/%d/",blank=True, null=True)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Description= RichTextField(blank=True, null=True)
    class Meta:
      ordering = ("-created_at",)
    def __str__(self):
         return self.Title
     
 