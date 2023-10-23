from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def children(request):
    return HttpResponse("This is the Children page")