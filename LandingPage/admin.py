from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from LandingPage.models import *
# # Register your models here.
 
 
class DescriptionAdmin(admin.TabularInline):
    model = LandingPageDescription

class BeforeAfterAdmin(admin.TabularInline):
    model = LandingPageBeforeAfter

class Imageadmin(admin.TabularInline):
    model = LandingPageImage

class ReviewsAdmin(admin.TabularInline):
    model = LandingPageReviews
 
class QuestionsAdmin(admin.TabularInline):
    model = LandingPageQuestions
 
class PriceAdmin(admin.TabularInline):
    model = LandingPagePrice
 
class LandingAdmin(admin.ModelAdmin):
    inlines = [Imageadmin ,DescriptionAdmin , BeforeAfterAdmin ,  ReviewsAdmin,QuestionsAdmin, PriceAdmin]
admin.site.register(LandingPage,LandingAdmin)
 
  
@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin):


    model = Booking
    # editable_list = ['STATUS']
    list_display = [ 'created_at','name','phone','knew','Message','landingPage','STATUS'  ]
    list_filter = ( 'created_at','name','phone','knew','Message','landingPage','STATUS'  )
 
 
 
 
 
 