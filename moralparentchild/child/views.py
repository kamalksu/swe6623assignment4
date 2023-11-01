from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Child
from .forms import Childform
from django.contrib import messages


# Create your views here.

def children(request):
    all_children = Child.objects.all().values()
    template = loader.get_template('dashboard.html')
    #return HttpResponse("This is the Children page")
    context = {
        'all_children' : all_children,
    }    
    return HttpResponse(template.render(context,request))


def child_apply(request):
    context = {}
    form = Childform(request.POST or None, request.FILES or None)

    if form.is_valid():
        firstname = form.cleaned_data['firstname']  
        lastname = form.cleaned_data['lastname']
        address = form.cleaned_data['zip_code']
        state = form.cleaned_data['state']
        country = form.cleaned_data['country']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        photo = form.cleaned_data['photo']
        school_name = form.cleaned_data['school_name']
        school_address = form.cleaned_data['school_address']
        fund_request_amount = form.cleaned_data['fund_request_amount']
        fund_request_months = form.cleaned_data['fund_request_months']
        login_id = form.cleaned_data['login_id']
        desription = form.cleaned_data['desription']
        supporting_document1 = form.cleaned_data['supporting_document1']
        supporting_document2 = form.cleaned_data['supporting_document2']
        form.save()
        form = Childform()
        messages.success(request, 'Form submission successful')
    
    context['form'] = form

    return render(request, "apply.html", context ) 