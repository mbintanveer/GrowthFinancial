from django.http import response
from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .serializers import ClientSerializer, InvoiceSerializer, ReceivingSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView


from .models import Client, Invoice_Entry,Receiving,Invoice
from itertools import chain
from operator import attrgetter

@api_view(['GET', 'POST']) #Post for new
def clients_list(request):
    if request.method == 'GET':
        client = Client.objects.all()
        client_name_keyword = request.GET.get('client_name_keyword', None)
        if client_name_keyword is not None:
            client = client.filter(client_name__icontains=client_name_keyword)
        
        client_serializer = ClientSerializer(client, many=True)
        return JsonResponse(client_serializer.data, safe=False)

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST', 'DELETE'])
# def client_list(request):
#     if request.method == 'GET':
#         clients = Client.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             clients = Client.filter(title__icontains=title)
        
#         clients_serializer = ClientSerializer(clients, many=True)
#         return JsonResponse(clients_serializer.data, safe=False)
  
@api_view(['GET','PUT','DELETE'])
def clients_detail(request, pk):  
    try: 
        client = Client.objects.get(pk=pk) 
    except Client.DoesNotExist: 
        return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        client_serializer = ClientSerializer(client) 
        return JsonResponse(client_serializer.data) 

    elif request.method == 'PUT': 
        client_data = JSONParser().parse(request) 
        client_serializer = ClientSerializer(client, data=client_data) 
        if client_serializer.is_valid(): 
            client_serializer.save() 
            return JsonResponse(client_serializer.data) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        client.delete() 
        return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

     
#INVOICES

@api_view(['GET', 'POST']) #Post for new
def invoices_list(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        invoice_serializer = InvoiceSerializer(invoice, many=True)
        return JsonResponse(invoice_serializer.data, safe=False)

    elif request.method == 'POST':
        invoice_data = JSONParser().parse(request)
        invoice_serializer = InvoiceSerializer(data=invoice_data)
        if invoice_serializer.is_valid():
            invoice_serializer.save()
            return JsonResponse(invoice_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def invoices_detail(request, pk):  
    try: 
        invoice = Invoice.objects.get(pk=pk) 
    except Invoice.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        invoice_serializer = InvoiceSerializer(invoice) 
        return JsonResponse(invoice_serializer.data) 

    elif request.method == 'PUT': 
        invoice_data = JSONParser().parse(request) 
        invoice_serializer = InvoiceSerializer(invoice, data=invoice_data) 
        if invoice_serializer.is_valid(): 
            invoice_serializer.save() 
            return JsonResponse(invoice_serializer.data) 
        return JsonResponse(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        invoice.delete() 
        return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
#RECEIVING

@api_view(['GET', 'POST']) #Post for new
def receivings_list(request):
    if request.method == 'GET':
        receiving = Receiving.objects.all()
        receiving_serializer = ReceivingSerializer(receiving, many=True)
        return JsonResponse(receiving_serializer.data, safe=False)

    elif request.method == 'POST':
        receiving_data = JSONParser().parse(request)
        receiving_serializer = ReceivingSerializer(data=receiving_data)
        if receiving_serializer.is_valid():
            receiving_serializer.save()
            return JsonResponse(receiving_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(receiving_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def receivings_detail(request, pk):  
    try: 
        receiving = Receiving.objects.get(pk=pk) 
    except Receiving.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        receiving_serializer = ReceivingSerializer(receiving) 
        return JsonResponse(receiving_serializer.data) 

    elif request.method == 'PUT': 
        receiving_data = JSONParser().parse(request) 
        receiving_serializer = ReceivingSerializer(receiving, data=receiving_data) 
        if receiving_serializer.is_valid(): 
            receiving_serializer.save() 
            return JsonResponse(receiving_serializer.data) 
        return JsonResponse(receiving_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        receiving.delete() 
        return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


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


def invoices_get_invoice_entries(request,pk):
    try: 
        invoice = Invoice.objects.get(pk=pk)
        invoice_entries =  Invoice_Entry.objects.filter(entry_invoice=invoice).values()
    except Invoice.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    return JsonResponse({"models_to_return": list(invoice_entries)},safe=False)
