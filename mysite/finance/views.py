from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Group, People, Category, LineItem
from .forms import PurchaseForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def person(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def person_summary(request,person_name,month,year):
    person = get_object_or_404(People,person_name=person_name)
    category_list = get_list_or_404(Category,person=person,month_number=month,year_number=year)
    months = [0,"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    month_name = months[month]
    context = {
        'person':person,
        'category_list':category_list,
        'month': month_name,
        'year': year
    }
    return render(request,'finance/person_summary.html',context)

def confirm(request):
    return HttpResponse("confirming your purchase here")

def purchase(request,person_name):
    person = get_object_or_404(People,person_name=person_name)
    category_list = person.category_set.filter(month_number=2,year_number=2019)
    context = {
        'person_name': person.person_name,
        'category_list': category_list,
    }        

    return render(request,'finance/purchase.html',context)


def purchase_2(request,person_name):
    person = get_object_or_404(People,person_name=person_name)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PurchaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/confirm/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PurchaseForm(person)

    return render(request, 'finance/purchase2.html', {'form': form})