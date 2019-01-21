from django.contrib import admin

from .models import Group, People, Category, LineItem

# Register your models here.
admin.site.register(Group)
admin.site.register(People)
admin.site.register(Category)
admin.site.register(LineItem)
