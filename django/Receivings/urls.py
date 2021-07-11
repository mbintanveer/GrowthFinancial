from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

path('', views.Receivings_Landing, name='Receivings_Landing'),
url(r'^api/Receivings$', views.receivings_list),
url(r'^api/Receivings/(?P<pk>[0-9]+)$', views.receivings_detail),

]