from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Home 1")
def contact(request):
    return HttpResponse("Contact")
def about(request):
    return HttpResponse("About")




