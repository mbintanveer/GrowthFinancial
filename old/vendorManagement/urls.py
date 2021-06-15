from django.urls import path
from . import views

urlpatterns = [

path('', views.vLanding, name='vLanding'),
path('vMgm', views.vMgm, name='vMgm'),
path('vCompleted', views.vCompleted,name='vCompleted'),
path('vAdd',views.vAdd,name='vAdd'),
path('vEdit/<int:id>/',views.vEdit,name='vEdit'),
path('vSpecific/<int:id>/',views.vSpecific,name= 'vSpecific'),
path('vSummary',views.vSummary,name='vSummary'),

#Functions
path('addVendorFunction',views.addVendorFunction,name='addVendorFunction'),
path('editVendorFunction',views.editVendorFunction,name='editVendorFunction'),

]

