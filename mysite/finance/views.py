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

def confirm(request):
    return HttpResponse("confirming your purchase here")

def purchase(request,person_name):
    person = get_object_or_404(People,person_name=person_name)
    category_list = person.category_set.filter(month_number=2,year_number=2019)
    context = {
        'group_name' : "texasCouple",
        'person_name': person.person_name,
        'category_list': category_list
    }
    return render(request,'finance/purchase.html',context)
