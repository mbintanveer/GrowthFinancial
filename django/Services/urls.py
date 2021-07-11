from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

url(r'^api/Services$', views.services_list),
url(r'^api/Services/(?P<pk>[0-9]+)$', views.services_detail),

path('', views.Services_Landing, name='Services_Landing'),
path('Services_Add', views.Services_Add, name='Services_Add'),
path('Recurring_Add', views.Recurring_Add, name='Recurring_Add'),


]

