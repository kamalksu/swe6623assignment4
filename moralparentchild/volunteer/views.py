from django.shortcuts import render
from django.http import HttpResponse
from .form import Volunteerform
from django.contrib import messages

# Create your views here.

def volunteers(request):
    return HttpResponse("This is volunteer page")



def volunteer_apply(request):
    context = {}
    form = Volunteerform(request.POST or None, request.FILES or None)

    if form.is_valid():
        firstname = form.cleaned_data['firstname']  
        lastname = form.cleaned_data['lastname']
        address = form.cleaned_data['address']
        zip_code = form.cleaned_data['zip_code']
        state = form.cleaned_data['state']
        country = form.cleaned_data['country']
        profession = form.cleaned_data['profession']  
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        photo = form.cleaned_data['photo']
        login_id = form.cleaned_data['login_id']
        desription = form.cleaned_data['desription']
        supporting_document1 = form.cleaned_data['supporting_document1']
        supporting_document2 = form.cleaned_data['supporting_document2']
        form.save()
        form = Volunteerform()
        messages.success(request, 'Form submission successful')
    
    context['form'] = form

    return render(request, "apply.html", context ) 