from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(reuqest):
    return render(reuqest, 'home/index.html')


def succes(reuqest):
    return HttpResponse("i am success....")  

def about(reuqest):
    return render(reuqest, 'home/about.html')

def contact(reuqest):
    return render(reuqest, 'home/contact.html')







