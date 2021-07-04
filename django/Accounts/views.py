from django.shortcuts import render
from Vendors.models import Vendors
from Clients.models import Client

# Create your views here.
def Accounts_Landing(request):
    VendorsList = Vendors.objects.all()
    ClientsList = Client.objects.all()

    vendor_one_month_summary_total=0
    vendor_two_month_summary_total=0
    vendor_three_month_summary_total=0
    vendor_four_month_summary_total=0
    vendor_all_month_summary_total =0
    client_one_month_summary_total=0
    client_two_month_summary_total=0
    client_three_month_summary_total=0
    client_four_month_summary_total=0
    client_all_month_summary_total =0

    for vendor in VendorsList:
        vendor_one_month_summary_total = vendor_one_month_summary_total + vendor.get_one_month()
        vendor_two_month_summary_total = vendor_two_month_summary_total + vendor.get_two_month()
        vendor_three_month_summary_total = vendor_three_month_summary_total + vendor.get_three_month()
        vendor_four_month_summary_total = vendor_four_month_summary_total + vendor.get_four_month()
        vendor_all_month_summary_total = vendor_all_month_summary_total + vendor.get_total()
    
    for client in ClientsList:
        client_one_month_summary_total = client_one_month_summary_total + client.get_one_month()
        client_two_month_summary_total = client_two_month_summary_total + client.get_two_month()
        client_three_month_summary_total = client_three_month_summary_total + client.get_three_month()
        client_four_month_summary_total = client_four_month_summary_total + client.get_four_month()
        client_all_month_summary_total = client_all_month_summary_total + client.get_total()
    
    params = {'VendorsList':VendorsList,'vendor_one_month_summary_total':vendor_one_month_summary_total,'vendor_two_month_summary_total':vendor_two_month_summary_total,
    'vendor_three_month_summary_total':vendor_three_month_summary_total, 'vendor_four_month_summary_total':vendor_four_month_summary_total, 
    'vendor_all_month_summary_total':vendor_all_month_summary_total, 'ClientsList':ClientsList,'client_one_month_summary_total':client_one_month_summary_total,
    'client_two_month_summary_total':client_two_month_summary_total,
    'client_three_month_summary_total':client_three_month_summary_total, 'client_four_month_summary_total':client_four_month_summary_total, 
    'client_all_month_summary_total':client_all_month_summary_total}

    return render(request,'Accounts_Landing.html',params)

