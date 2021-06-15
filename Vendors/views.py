
from django.shortcuts import render
from .models import Vendors, Bills, Payments
from itertools import chain
from operator import attrgetter

Bills = Bills.objects.all()

def Vendors_Landing(request):
    VendorsList = Vendors.objects.all()
    params = {'VendorsList':VendorsList}
    
    return render(request,'Vendors_Landing.html',params)

def Vendors_View(request,id):
    from .models import Bills, Payments

    vendor =  Vendors.objects.get(pk=id)
    Bills=Bills.objects.filter(bill_vendor=vendor)
    Payments = Payments.objects.filter(payment_vendor=vendor)
    combined_results = sorted(
    chain(Bills, Payments),
    key=attrgetter('date_created'),reverse=True)

    params= {'vendor':vendor,'combined_results':combined_results}

    return render(request,'Vendors_View.html',params)

