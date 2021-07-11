from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .serializers import ClientSerializer, InvoiceSerializer, ReceivingSerializer
from rest_framework.decorators import api_view

from .models import Client,Receiving,Invoice
from itertools import chain
from operator import attrgetter



# Create your views here.
def Clients_Landing(request):
    ClientsList = Client.objects.all()
    params = {'ClientsList':ClientsList}
    return render(request,'Clients_Landing.html',params)
    


def Clients_View(request,id):
    client =  Client.objects.get(pk=id)
    Invoices=Invoice.objects.filter(invoice_client=client)
    Receivings = Receiving.objects.filter(receiving_client=client)
    combined_results = sorted(
    chain(Invoices, Receivings),
    key=attrgetter('date_created'),reverse=True)
    params= {'client':client,'combined_results':combined_results}
    return render(request,'Clients_View.html',params)

@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    if request.method == 'GET':
        Client = Client.objects.all()
        client_serializer = ClientSerializer(Client, many=True)
        return JsonResponse(client_serializer.data, safe=False)


    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_detail(request, pk):  
    try: 
        client = Client.objects.get(pk=pk) 
        if request.method == 'GET': 
            client_serializer = ClientSerializer(client) 
        return JsonResponse(client_serializer.data) 
    except Client.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def invoice_detail(request, pk):  
    try: 
        invoice = Invoice.objects.get(pk=pk) 
        if request.method == 'GET': 
            invoice_serializer = InvoiceSerializer(invoice) 
        return JsonResponse(invoice_serializer.data) 
    except Invoice.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def receiving_detail(request, pk):  
    try: 
        receiving = Receiving.objects.get(pk=pk) 
        if request.method == 'GET': 
            receiving_serializer = ReceivingSerializer(receiving) 
        return JsonResponse(receiving_serializer.data) 
    except Receiving.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

# @api_view(['GET'])
# def tutorial_list_published(request):
#     # GET all published tutorials