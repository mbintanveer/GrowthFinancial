from django.urls import path
from . import views

urlpatterns = [

path('', views.Vendors_Landing, name='Vendors_Landing'),
path('Vendors_View/<int:id>/', views.Vendors_View, name='Vendors_View')

]