"""GrowthFinancial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path,include
from . import view

urlpatterns = [

    url(r'^', include('Clients.urls')),

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
