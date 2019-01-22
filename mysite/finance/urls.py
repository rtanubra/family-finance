from django.urls import path
from . import views 

app_name = 'finance'
urlpatterns = [
    #/finance/
    path("",views.index, name= 'index'),
    #/finance/rey_tanubrata/purchase/
    path("<str:person_name>/purchase/",views.purchase, name='results'),
    #/finance/confirm
    path('confirm/',views.confirm,name='confirm')
]