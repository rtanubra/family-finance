from django.urls import path
from . import views 

app_name = 'finance'
urlpatterns = [
    #/finance/
    path("",views.index, name= 'index'),
    #/finance/Rey/purchase/
    path("<str:person_name>/purchase/",views.purchase, name='purchase'),
    #/finance/Rey/purchase2/  -- under development using Form class
    path("<str:person_name>/purchase2/",views.purchase_2, name='purchase2'),
    #finance/Rey/2_2019/
    path("<str:person_name>/<int:month>_<int:year>/",views.person_summary, name= 'summary'),
    #/finance/confirm
    path('confirm/',views.confirm,name='confirm')
]