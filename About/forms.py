from django import forms
from LandingPage.models import *      
from django.contrib.admin import widgets
     
        
class  booking(forms.ModelForm):
 
      required_css_class = 'required'

      def __init__(self, *args, **kwargs):
              super(booking, self).__init__(*args, **kwargs)

              self.fields['name'].widget.attrs['placeholder'] = 'الاسم'
              self.fields['Message'].widget.attrs['placeholder'] = 'ملاحظه'
              self.fields['phone'].widget.attrs['placeholder'] = 'رقم الهاتف'
  
      
 
      class Meta:
           model = Booking      
           fields = ('name','phone','knew','Message')    
           exclude = ['created_at','LandingPage', 'STATUS' ]   
      
  