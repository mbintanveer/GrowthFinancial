from django.urls import path
from . import views

urlpatterns = [

path('', views.Receivings_Landing, name='Receivings_Landing'),

]