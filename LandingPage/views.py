from django.shortcuts import render, redirect
from LandingPage.models import *
# import pandas as pd
from LandingPage.forms import *
from django.shortcuts import render, get_object_or_404
# # Create your views here.
def landingpage(request):
    Landing =LandingPage.objects.filter(active=True)
 
    context = {
   
        'Landing':Landing,
 
    
    } 
    return render(request, 'services.html', context) 


 
def landingPageDetails(request, slug):
 
    PageDetails = get_object_or_404(LandingPage,slug=slug)

    if request.method=='POST':
        form= bookingLandingPage(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)    
            myform.landingPage=PageDetails 
            myform.save()

            print('DOne')  
            context = {
            'form':form,
            'PageDetails':PageDetails}
 
 
            return  redirect ('Landingpage:LandingAll') 
    else:
        form = bookingLandingPage()
        print('404')  
 
    context = {
   
       'landingPage':PageDetails,
       'form':form,
    
    } 
    return render(request, 'LandingPage.html', context)

# def landingpage(request, slug):
#     landingPage = get_object_or_404(LandingPage,slug=slug)
#     data =LandingPage.objects.filter(slug=landingPage).values() 
#     print(data )
#     data_df = pd.DataFrame(data)
#     data_web=data_df["WebName"] 
#     print(data_web )
#     data_web1=data_web.tolist()
#     print(data_web1 )
#     data_web2=data_web1[0]
#     print(data_web2 )
#     if request.method=='POST':
#         form= bookingLandingPage(request.POST)
#         if form.is_valid():
#            myform = form.save(commit=False)    
#            myform.LandingPage=landingPage 
#            myform.web=data_web2 
#            myform.save()

#            print('DOne')  
#         #    context = {
#         #     'form':form,
#         #       'landingPage':landingPage}
#         #    return render(request, 'offer.html', context)
#     else:
#         form = bookingLandingPage()
#         print('404') 
 
#     context = {
#    'form':form,
#        'landingPage':landingPage
 
    
#     } 
 
#     return render(request, 'offer.html', context)

 
# def doctor(request, slug):
#     doctoR = get_object_or_404(Doctors,slug=slug)
#     # if request.method=='POST':
#     #     form= booking(request.POST)

#     #     if form.is_valid():
#     #         myform = form.save(commit=False)
#     #         myform.price=PriceServicesdetails
#     #         form.save()

#     #         print('DOne')      
#     #         return redirect ('Services:BookingSuccess') 
#     # else:
#     #     form = booking()
 
 
#     context = {
   
#        'doctor':doctoR,
#     #    'form':form
    
#     } 
 
#     return render(request, 'doctor.html', context)

















# # def Booking(request):   
# #     if request.method=='POST':
# #         Bookingform= booking(request.POST)

# #         if Bookingform.is_valid():
# #             myform = Bookingform.save(commit=False)
# #             myform.save() 
# #             return redirect ('Services:BookingSuccess') 
# #     else:
# #         Bookingform = booking()
 
 
# #     context = {
   
  
# #        'Bookingform':Bookingform
# #         } 
 
# #     return render(request, 'ContactUs.html', context)   
# # def Bookingsuccess(request):
# #     servicesGuide =Guide.objects.filter(active=True)
# #     servicesModern =Modern.objects.filter(active=True)
# #     servicesSample =Sample.objects.filter(active=True) 
# #     servicesPrice =Price.objects.filter(active=True)    
    
   
# #     context = {  
# #      'servicesGuide':servicesGuide ,
# #      'servicesModern':servicesModern,    
# #      'servicesSample':servicesSample,   
# #      'servicesPrice':servicesPrice, } 

# #     return render(request, 'servicessuccess.html', context) 
   
 
 
         
    
 