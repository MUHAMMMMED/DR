
from django.db import models
from django.utils.text import slugify
# Property models here.

class ServicesProperty(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default = False)
   Image = models.FileField(upload_to = "files/images/LandingPage/photos/Image/%Y/%m/%d/",blank=True, null=True)
   ImageName = models.CharField(max_length = 300 ,blank=True, null=True)
   slideImage = models.FileField(upload_to = "files/images/LandingPage/photos/slideImage/%Y/%m/%d/",blank=True, null=True)
   Title = models.CharField(max_length=100)
   Description = models.CharField(max_length = 500 ,blank=True, null=True)
   price = models.CharField(max_length=100,blank=True, null=True)
   discount= models.CharField(max_length=100,blank=True, null=True)
   DoctorImage = models.FileField(upload_to = "files/images/Doctors/photos/%Y/%m/%d/",blank=True, null=True)
   DoctorName = models.CharField(max_length = 300 ,blank=True, null=True)
   Doctorjobtitle= models.CharField(max_length = 300 ,blank=True, null=True)
   DoctorDescription= models.CharField(max_length = 300 ,blank=True, null=True)
   QuestionsTitle= models.CharField(max_length = 300 ,blank=True, null=True)
   slug = models.SlugField(unique = True,blank=True, null=True)
   
   class Meta:
     ordering = ("-created_at",)


   def save(self,*args, **kwargs):
        self.slug = slugify(self.Title)
        super(ServicesProperty,self).save(*args, **kwargs)


   def __str__(self):
        return self.Title
   
 # LandingPage models here.
class LandingPage(ServicesProperty):    
     pass
   
class LandingPageBeforeAfter(models.Model):
    lndingPageBeforeAfter = models.ForeignKey(LandingPage, related_name='beforeafter', on_delete=models.CASCADE)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Description = models.CharField(max_length = 500 ,blank=True, null=True)
    Image = models.FileField(upload_to = "files/images/LandingPageBeforeAfter/photos/Image/%Y/%m/%d/",blank=True, null=True)
   
    def __str__(self):
         return self.Title
    
class LandingPagePrice(models.Model):
    lndingPagePrice = models.ForeignKey(LandingPage, related_name='Price', on_delete=models.CASCADE)
    Title = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
         return self.Title
     
class LandingPageQuestions(models.Model):
    lndingPageQuestions = models.ForeignKey(LandingPage, related_name='questions', on_delete=models.CASCADE)
    question= models.CharField(max_length = 300 ,blank=True, null=True)
    answer = models.CharField(max_length=300,blank=True, null=True)
    
    def __str__(self):
         return self.question

class LandingPageImage(models.Model):
     lndingPageImage = models.ForeignKey(LandingPage, related_name='image', on_delete=models.CASCADE)
     Image = models.FileField(upload_to = "files/images/LandingPageImage/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     
     def __str__(self):
          return self.Name

class LandingPageReviews(models.Model):
     lndingPageReviews = models.ForeignKey(LandingPage, related_name='Reviews', on_delete=models.CASCADE)
     Image = models.FileField(upload_to = "files/images/LandingPageReviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     
     def __str__(self):
        return self.Name
   
class LandingPageDescription(models.Model):
      lndingPageDescription = models.ForeignKey(LandingPage, related_name='description', on_delete=models.CASCADE)
      Titel = models.CharField(max_length=100,blank=True, null=True)
      Description= models.CharField(max_length = 500 ,blank=True, null=True)
      
      def __str__(self):
         return self.Titel


  
class Booking(models.Model):
 
    Undefined="كيف عرفتنا"
    insurance='تأمين'
    Friend='صديق '   
    family='أسرة'
    neighbors='الجيران'
    Google='جوجل '  
    Whatsapp ='واتساب'
    snapchat='سناب' 
    Instagram='انستقرام'
    Twitter='تويتر'    
    Facebook='فيس بوك '
    ticktock='تيك توك'
    YouTube='يوتيوب ' 
    Email='البريد الإلكتروني'  
    Site='موقع'  
    other='آخر'

    CHOICES_knew = (
    (Undefined,"كيف عرفتنا"),
    (insurance,'تأمين'),
    (Friend,'صديق '),
    (family,'أسرة'),
    (neighbors,'الجيران'),
    (Google,'جوجل '),
    (Whatsapp,'واتساب'),
    (snapchat,'سناب'),
    (Instagram,'انستقرام'),
    (Twitter,'تويتر'),
    (Facebook,'فيس بوك '),
    (ticktock,'تيك توك'),
    (YouTube,'يوتيوب '), 
    (Email,'البريد الإلكتروني'),
    (Site,' موقع الإلكتروني'),
    (other,'آخر'),
        
  )  
    waiting = 'انتظار'
    booking = 'حجز غير مؤكد'
    Reservationconfirmed="حجز مؤكد"
    cancel ='إلغاءحجزه'
    Visit =  'حضر'
    CHOICES_STATUS = (( waiting,'انتظار'),(booking,'حجز غير مؤكد'),(Reservationconfirmed,"حجز مؤكد"),(cancel,'إلغاءحجزه'),(Visit,'حضر')) 
 
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    landingPage = models.ForeignKey(LandingPage, on_delete=models.CASCADE,blank=True, null=True)
    knew = models.CharField(max_length=50, choices=CHOICES_knew, default=Undefined)
    Message= models.CharField(max_length=500)
    STATUS = models.CharField(max_length=50, choices=CHOICES_STATUS, default=waiting )
 
    def __str__(self):
        return self.name

# Visiblenumbers Django App