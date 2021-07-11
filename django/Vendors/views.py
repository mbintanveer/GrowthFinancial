
from django.shortcuts import render
from .models import Vendors, Bills, Payments
from rest_framework.decorators import api_view
from itertools import chain
from operator import attrgetter
from .serializers import VendorSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

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

@api_view(['GET','POST'])
def vendors_list(request):
    if request.method == 'GET':
        vendor = Vendors.objects.all()
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
        return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        