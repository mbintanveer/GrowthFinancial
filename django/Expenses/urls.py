from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

url(r'^api/Expenses$', views.expense_list),
url(r'^api/Expenses/(?P<pk>[0-9]+)$', views.expense_detail),

path('', views.Expenses_Landing, name='Expenses_Landing'),

]