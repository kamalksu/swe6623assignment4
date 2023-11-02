from django import forms
from .models import Parent

class Parentform(forms.ModelForm):
    class Meta:
        model = Parent
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
                  'possible_funding',
                  'login_id',
                  'desription',
                  'supporting_document1',
                  'supporting_document2']
