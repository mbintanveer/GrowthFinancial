from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
url(r'^api/Vendors$', views.vendors_list),
url(r'^api/Vendors/(?P<pk>[0-9]+)$', views.vendors_detail),


path('', views.Vendors_Landing, name='Vendors_Landing'),
path('Vendors_View/<int:id>/', views.Vendors_View, name='Vendors_View')

]