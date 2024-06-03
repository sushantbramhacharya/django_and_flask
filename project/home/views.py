from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello this is home app")

def products(request):
    return HttpResponse("This is products page")