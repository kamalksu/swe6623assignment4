from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def parents(request): 
    template = loader.get_template('parentDashboard.html')
    return HttpResponse(template.render())