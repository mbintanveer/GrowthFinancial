from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^api/Clients$', views.client_list),
url(r'^api/Clients/(?P<pk>[0-9]+)$', views.client_detail),
# url(r'^api/Clients/published$', views.client_list_published),

# path('', views.Clients_Landing, name='Clients_Landing'),
# path('Clients_View/<int:id>/', views.Clients_View, name='Clients_View'),

]

