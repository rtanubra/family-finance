from django import forms
import datetime
from .models import Group, Category, People, LineItem

class PurchaseForm(forms.Form):
    def __init__(self,person):
        super().__init__()
        self.person = person
        self.category_list = person.category_set.filter(month_number=2,year_number=2019)
        self.make_category()
    c = [
        ("1","Credit"),
        ("2","Debit/Cash"),
        ("3","Pay off Credit")
    ]
    def make_category(self):
        self.category = forms.ModelChoiceField(queryset=self.category_list)

    description = forms.CharField(max_length=100)
    purchase_date = forms.DateField(initial=datetime.date.today)
    amount = forms.DecimalField(max_digits=8,decimal_places=2)
    method = forms.ChoiceField(choices=c, label="Method of Payment")

