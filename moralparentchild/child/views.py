from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Child

# Create your views here.

def children(request):
    all_children = Child.objects.all().values()
    #template = loader.get_template('')
    return HttpResponse("This is the Children page")