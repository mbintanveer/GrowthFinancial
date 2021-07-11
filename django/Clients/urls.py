from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^api/Clients$', views.client_list),
url(r'^api/Clients/(?P<pk>[0-9]+)$', views.client_detail),

url(r'^api/Invoices/(?P<pk>[0-9]+)$', views.invoice_detail),

url(r'^api/Receivings/(?P<pk>[0-9]+)$', views.receiving_detail),




# path('', views.Clients_Landing, name='Clients_Landing'),
# path('Clients_View/<int:id>/', views.Clients_View, name='Clients_View'),

]

