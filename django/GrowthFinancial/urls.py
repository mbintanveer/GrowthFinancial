

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path,include
from . import view

urlpatterns = [

    url(r'^', include('Clients.urls')),
    url(r'^', include('Expenses.urls')),

    path('Services/', include('Services.urls')),
    path('Clients/',include('Clients.urls')),
    path('Expenses/', include('Expenses.urls')),
    path('Receivings/',include('Receivings.urls')),
    path('Accounts/',include('Accounts.urls')),
    path('Vendors/',include('Vendors.urls')),
    
    #Default
    path('', view.index, name='index'),
    path('admin/', admin.site.urls,name='admin'),
    path('signIn/',view.signIn,name='signIn'),
    path('signOut/',view.signOut,name='signOut'),
    path('unavailable/',view.unavailable,name='unavailable')
]
