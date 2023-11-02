from django import forms
from .models import Volunteer

class Volunteerform(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['firstname', 
                  'lastname', 
                  'address', 
                  'state', 
                  'country',
                  'zip_code',
                  'profession', 
                  'phone', 
                  'email',
                  'photo',
                  'login_id',
                  'desription',
                  'supporting_document1',
                  'supporting_document2']
