from django.urls import path
from . import views

urlpatterns = [

path('', views.iLanding, name='iLanding'),
path('iEdit/<int:id>/',views.iEdit,name='iEdit'),
path('iMgm', views.iMgm, name='iMgm'),
path('iSpecific/<int:id>/',views.iSpecific,name= 'iSpecific'),
path('iSummary',views.iSummary,name='iSummary'),
path('iCompleted', views.iCompleted,name='iCompleted'),
path('iAdd',views.iAdd,name='iAdd'),


path('removeInvoiceFunction/<int:id>/', views.removeInvoiceFunction, name='removeInvoiceFunction'),
path('addInvoiceFunction',views.addInvoiceFunction,name='addInvoiceFunction'),
path('editInvoiceFunction',views.editInvoiceFunction,name='editInvoiceFunction'),


]
