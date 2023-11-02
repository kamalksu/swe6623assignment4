from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from child.models import Child

# Create your views here.

def home(request): 
    all_children = Child.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'all_children' : all_children,
    }    
    return HttpResponse(template.render(context,request))



def child_detail(request, id):
    child = Child.objects.get(id=id)
    template = loader.get_template('child_detail.html')
    context = {
        'child' : child,
    }
    return HttpResponse(template.render(context,request))