from django.db import models

# Create your models here.
class Group(models.Model):
    
    def __str__(self):
        return self.group_name
    
    group_name = models.CharField(max_length=200,unique=True)


class People(models.Model):

    def __str__(self):
        return self.person_name

    group_couple = models.ForeignKey(Group,on_delete=models.CASCADE)
    person_name= models.CharField(max_length=70)
    username = models.CharField(max_length=70,unique=True)


class Category(models.Model):

    def unique_month_year(self,month_number,year_number):
        #For this specific group this category name must only appear once with this month and unique number
        pass 

    def __str__(self):
        return self.category_name

    #group =models.ForeignKey(Group,on_delete=models.CASCADE)
    person = models.ForeignKey(People,on_delete=models.CASCADE)
    #each category will roll up to one group. 
    ##uncessary because if we roll up to one person we roll up to a single group.
    category_name = models.CharField(max_length=100)
    category_total = models.DecimalField(max_digits=8,decimal_places=2)
    category_spent = models.DecimalField(max_digits=8,decimal_places=2)
    category_left = models.DecimalField(max_digits=8,decimal_places=2)
    month_number = models.PositiveSmallIntegerField()
    year_number = models.PositiveSmallIntegerField()
    

class LineItem(models.Model):
    
    def __str__(self):
        return self.description
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #by = models.ForeignKey(People,on_delete=models.CASCADE)
    ## unecessary because if we roll up to a single category then by definition roll up to one person
    description = models.CharField(max_length=200)
    purchase_date = models.DateField()
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    pmt_type = models.CharField(max_length=200) #SHOULD BE 3 choices in entry world.
    #1.Credit 2.Debit/cash 3.Paid_off_credit_card
    