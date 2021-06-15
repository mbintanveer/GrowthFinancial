from django.urls import path
from . import views

urlpatterns = [

#Pages
path('', views.pLanding, name='pLanding'),
path('pMgm', views.pMgm, name='pMgm'),
path('pAdd',views.pAdd,name='pAdd'),
path('pEdit/<int:id>/',views.pEdit,name='pEdit'),
path('pSummary',views.pSummary,name='pSummary'),
path('pSpecific/<int:id>/', views.pSpecific, name='pSpecific'),

#Functions
path('addProjectFunction',views.addProjectFunction, name='addProjectFunction'),
path('editProjectFunction',views.editProjectFunction, name='editProjectFunction'),
]
