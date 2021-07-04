from django.urls import path
from . import views

urlpatterns = [

path('', views.Expenses_Landing, name='Expenses_Landing'),

]