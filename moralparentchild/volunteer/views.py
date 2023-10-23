from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def volunteers(request):
    return HttpResponse("This is volunteer page")