from django import forms
from .models import Volunteer
from child.models import ListofMoralChild
from parent.models import ListofMoralParent

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


class ChildApprovalForm(forms.ModelForm):
    class Meta:
        model = ListofMoralChild
        fields = [
            'fund_approved',
            'child_id',
            'background_checked',
            'approved',
            'comments',
            'parent_id'
        ]

class ParentApprovalForm(forms.ModelForm):
    class Meta:
        model = ListofMoralParent
        fields = [
            'possible_funding',
            'parent_id',
            'background_checked',
            'approved',
            'comments',
            'child_id'
        ]


