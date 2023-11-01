from django import forms
from .models import Child

class Childform(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['firstname', 
                  'lastname', 
                  'address', 
                  'state', 
                  'country',
                  'zip_code', 
                  'phone', 
                  'email',
                  'photo',
                  'school_name',
                  'school_address',
                  'fund_request_amount',
                  'fund_request_months',
                  'login_id',
                  'desription',
                  'supporting_document1',
                  'supporting_document2']
