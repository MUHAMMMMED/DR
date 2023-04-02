from django.db import models
from django.urls import reverse
 
from ckeditor.fields import RichTextField
 
# Create your models here.
class Blog(models.Model):#  
   active = models.BooleanField(default = False)
   Image = models.FileField(upload_to = "files/images/Blog/Image/%Y/%m/%d/",blank=True, null=True)
   Titel= models.CharField(max_length = 300 , null = True)
   Description = models.CharField(max_length = 300 , null = True) 
   slideImage =models.FileField(upload_to = "files/images/Blog/slideImage/%Y/%m/%d/",blank=True, null=True)
   body= RichTextField()
 

   def __str__(self):
        return self.Titel