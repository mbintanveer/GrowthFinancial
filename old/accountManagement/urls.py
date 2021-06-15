from django.urls import path

from . import views

urlpatterns = [
            #Pages
    path('', views.aLanding, name='aLanding'),
    path('aMgm',views.aMgm,name='aMgm'),
    path('aSummary',views.aSummary,name='aSummary'),
    path("addGeneralExpense", views.addGeneralExpense, name="addGeneralExpense"),
    path("addVendorExpense",views.addVendorExpense,name="addVendorExpense"),
    path('viewGeneralExpense/<int:id>/',views.viewGeneralExpense,name='viewGeneralExpense'),
    path('viewVendorExpense/<int:id>/', views.viewVendorExpense, name='viewVendorExpense'),
    path('editGeneralExpense/<int:primaryKey>/',views.editGeneralExpense,name='editGeneralExpense'),
    path('editVendorExpense/<int:primaryKey>/', views.editVendorExpense, name='editVendorExpense'),
    path('allVendorExpense',views.allVendorExpense,name='allVendorExpense'),
    path('allGeneralExpense',views.allGeneralExpense,name='allGeneralExpense'),

            #FUNCTIONS

    path("addGeneralExpenseFunction", views.addGeneralExpenseFunction, name="addGeneralExpenseFunction"),
    path("addVendorExpenseFunction", views.addVendorExpenseFunction, name="addVendorExpenseFunction"),
    path('editGeneralExpenseFunction', views.editGeneralExpenseFunction, name='editGeneralExpenseFunction'),
    path('editVendorExpenseFunction', views.editVendorExpenseFunction, name='editVendorExpenseFunction'),
]
