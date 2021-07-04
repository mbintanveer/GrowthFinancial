from django.urls import reverse
from django.shortcuts import render
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
