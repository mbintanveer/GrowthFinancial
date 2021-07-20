from django.shortcuts import render
from .models import Vendors, Bills, Payments
from rest_framework.decorators import api_view
from itertools import chain
from operator import attrgetter
from .serializers import VendorSerializer,BillSerializer,PaymentSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http import HttpResponse
import json


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

@api_view(['GET','POST'])
def vendors_list(request):
    if request.method == 'GET':
        vendor = Vendors.objects.all()
        vendor_name_keyword = request.GET.get('vendor_name_keyword', None)
        if vendor_name_keyword is not None:
            vendor = vendor.filter(vendor_name__icontains=vendor_name_keyword)
        vendor_serializer = VendorSerializer(vendor, many=True)
        return JsonResponse(vendor_serializer.data, safe=False)

    elif request.method == 'POST':
        vendor_data = JSONParser().parse(request)
        vendor_serializer =VendorSerializer(data=vendor_data)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse(vendor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vendors_detail(request, pk):  
    try: 
        vendor = Vendors.objects.get(pk=pk) 
    except Vendors.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        vendor_serializer = VendorSerializer(vendor) 
        return JsonResponse(vendor_serializer.data) 

    elif request.method == 'PUT': 
        vendor_data = JSONParser().parse(request) 
        vendor_serializer = VendorSerializer(vendor, data=vendor_data) 
        if vendor_serializer.is_valid(): 
            vendor_serializer.save() 
            return JsonResponse(vendor_serializer.data) 
        return JsonResponse(vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        vendor.delete() 
        return JsonResponse({'message': 'Vendor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
#INVOICES

@api_view(['GET', 'POST']) #Post for new
def bills_list(request):
  
    if request.method == 'GET':
        bill = Bills.objects.all()
        bill_vendor_id = request.GET.get('bill_vendor_id', None)
        if bill_vendor_id is not None:
            bill = bill.filter(bill_vendor=bill_vendor_id)
        
        bill_serializer = BillSerializer(bill, many=True)
        return JsonResponse(bill_serializer.data, safe=False)

    elif request.method == 'POST':
        bill_data = JSONParser().parse(request)
        bill_serializer = BillSerializer(data=bill_data)
        if bill_serializer.is_valid():
            bill_serializer.save()
            return JsonResponse(bill_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def bills_detail(request, pk):  
    try: 
        bill = Bills.objects.get(pk=pk) 
    except Bills.DoesNotExist: 
        return JsonResponse({'message': 'The Bill does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        bill_serializer = BillSerializer(bill) 
        return JsonResponse(bill_serializer.data) 

    elif request.method == 'PUT': 
        bill_data = JSONParser().parse(request) 
        bill_serializer = BillSerializer(bill, data=bill_data) 
        if bill_serializer.is_valid(): 
            bill_serializer.save() 
            return JsonResponse(bill_serializer.data) 
        return JsonResponse(bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        bill.delete() 
        return JsonResponse({'message': 'Bills was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
#RECEIVING

@api_view(['GET', 'POST']) #Post for new
def payments_list(request):
    if request.method == 'GET':
        payment = Payments.objects.all()
        payment_vendor_id = request.GET.get('payment_vendor_id', None)
        if payment_vendor_id is not None:
            payment = payment.filter(payment_vendor=payment_vendor_id)
        
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

    elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def payments_detail(request, pk):  
    try: 
        payment = Payments.objects.get(pk=pk) 
    except Payments.DoesNotExist: 
        return JsonResponse({'message': 'The Payment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment) 
        return JsonResponse(payment_serializer.data) 

    elif request.method == 'PUT': 
        payment_data = JSONParser().parse(request) 
        payment_serializer = PaymentSerializer(payment, data=payment_data) 
        if payment_serializer.is_valid(): 
            payment_serializer.save() 
            return JsonResponse(payment_serializer.data) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        payment.delete() 
        return JsonResponse({'message': 'Bills was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def vendors_summary(request, pk):  
    try: 
        vendor = Vendors.objects.get(pk=pk) 
    except Vendors.DoesNotExist: 
        return JsonResponse({'message': 'The Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        return get_vendor_summary(vendor)


@api_view(['GET'])
def all_vendors_summary(request):
    vendors= Vendors.objects.all()
    VendorResponse=[]
    for vendor in vendors:
        VendorResponse.append({"vendor_name":vendor.vendor_name,
            "get_one_month": vendor.get_one_month(),
            "get_two_month" : vendor.get_two_month(),
            "get_three_month":vendor.get_three_month(),
            "get_four_month":vendor.get_four_month(),
            "get_total":vendor.get_total()
            })

    return JsonResponse(VendorResponse,safe=False)


def get_vendor_summary(vendor):
    return JsonResponse(
            {"vendor_name":vendor.vendor_name,
            "get_one_month": vendor.get_one_month(),
            "get_two_month" : vendor.get_two_month(),
            "get_three_month":vendor.get_three_month(),
            "get_four_month":vendor.get_four_month(),
            "get_total":vendor.get_total()
            })

    # return JsonResponse(
    #         {"vendor_name":vendor.vendor_name,
    #         "get_one_month": vendor.get_one_month(),
    #         "get_two_month" : vendor.get_two_month(),
    #         "get_three_month":vendor.get_three_month(),
    #         "get_four_month":vendor.get_four_month(),
    #         "get_total":vendor.get_total()
    #         })

