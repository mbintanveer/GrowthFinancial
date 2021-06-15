from django.urls import path
from . import views

urlpatterns = [

path('', views.Accounts_Landing, name='Accounts_Landing'),

]