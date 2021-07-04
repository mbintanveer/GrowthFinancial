from django.urls import path
from . import views

urlpatterns = [

path('', views.Services_Landing, name='Services_Landing'),
path('Services_Add', views.Services_Add, name='Services_Add'),
path('Recurring_Add', views.Recurring_Add, name='Recurring_Add'),


]

