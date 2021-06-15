from django.urls import path
from . import views

urlpatterns = [

path('', views.Clients_Landing, name='Clients_Landing'),
path('Clients_View/<int:id>/', views.Clients_View, name='Clients_View'),

]

