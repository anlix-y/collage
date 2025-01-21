from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request): 
    return HttpResponse('привет мир')

def home(request):
    return render(request, 'home.html')


# Create your views here.
