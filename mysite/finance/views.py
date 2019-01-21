from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Group, People, Category, LineItem
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def person(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def person_summary(request,person,month_year):
    return HttpResponse("Hello, world. You are at the polls index.")

def purchase(request):
    return HttpResponse("Hello, world. You are at the polls index.")
