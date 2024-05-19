from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You are at Django home page")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Hello, world. You are at Django about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at Django contact page")
    return render(request, 'contact.html')

