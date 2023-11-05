from django.shortcuts import render
from django.http import HttpResponse
from .form import Volunteerform, ChildApprovalForm, ParentApprovalForm
from .models import Volunteer
from django.contrib import messages
from child.models import Child, ListofMoralChild
from parent.models import Parent, ListofMoralParent
from django.template import loader

# Create your views here.

def volunteers(request, id):
    login_id = 'volunteer1'
    #volunteer = Volunteer.objects.get(login_id=login_id)
    volunteer = Volunteer.objects.get(id=id)
    all_children = Child.objects.all().values()
    all_parents = Parent.objects.all().values()

    all_children_approved = ListofMoralChild.objects.all().values()
    all_parents_approved = ListofMoralParent.objects.all().values()

    context = {
        'volunteer' : volunteer,
        'all_children' : all_children,
        'all_parents' : all_parents,
        'all_children_approved' : all_children_approved,
        'all_parents_approved' : all_parents_approved

    }
    return render(request,"dashboard_volunteer.html", context)



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

def child_detail(request, id):
    login_id = 'volunteer1'
    volunteer = Volunteer.objects.get(login_id=login_id)
    child = Child.objects.get(id=id)
    #list_of_moral_child = ListofMoralChild.objects.get(id=id) 
    form = ChildApprovalForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        fund_approved = form.cleaned_data['fund_approved']
        form.save()
        form = ChildApprovalForm()
        messages.success(request, 'Child approval process completed. ')
    template = loader.get_template('child_approval.html')

    context = {
        'child' : child,
        'volunteer' : volunteer,
        'form' : form
    }
    return HttpResponse(template.render(context,request))



def parent_detail(request, id):
    login_id = 'volunteer1'
    volunteer = Volunteer.objects.get(login_id=login_id)
    parent = Parent.objects.get(id=id)
    #list_of_moral_child = ListofMoralChild.objects.get(id=id) 
    form = ParentApprovalForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        possible_funding = form.cleaned_data['possible_funding']
        form.save()
        form = ParentApprovalForm()
        messages.success(request, 'Parent approval process completed. ')
    template = loader.get_template('parent_approval.html')

    context = {
        'parent' : parent,
        'volunteer' : volunteer,
        'form' : form
    }
    return HttpResponse(template.render(context,request))