from Services.models import Service
import os
from django.db import models
import datetime
from datetime import date,datetime
from datetime import timedelta
from django.db.models import Sum

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    
    def get_one_month(self): #NO UPPER BOUND AS WE GET > 30 Days
        now = datetime.now()
        date_lower = now - timedelta(days=30)
        client_invoices = Invoice.objects.filter(invoice_client=self).filter(date_created__gte=date_lower)
        client_invoices_sum = client_invoices.aggregate(Sum('invoice_amount'))['invoice_amount__sum']
        if client_invoices_sum == None:
            client_invoices_sum = 0

        client_payments = Receiving.objects.filter(receiving_client=self).filter(date_created__gte=date_lower)
        client_payments_sum = client_payments.aggregate(Sum('receiving_amount'))['receiving_amount__sum']
        if client_payments_sum == None:
            client_payments_sum = 0
        payable_amount = client_invoices_sum - client_payments_sum
        return payable_amount

    def get_two_month(self):
        now = datetime.now()
        date_lower = now - timedelta(days=60)
        date_upper = now - timedelta(days=30)

        client_invoices = Invoice.objects.filter(invoice_client=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        # client_invoices_sum = client_invoices.aggregate(Sum('invoice_amount'))['invoice_amount__sum']
        # if client_invoices_sum == None:
        client_invoices_sum = 0

        client_payments = Receiving.objects.filter(receiving_client=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        client_payments_sum = client_payments.aggregate(Sum('receiving_amount'))['receiving_amount__sum']
        if client_payments_sum == None:
            client_payments_sum = 0

        payable_amount = client_invoices_sum - client_payments_sum
        return payable_amount

    def get_three_month(self):
        now=datetime.now()
        date_lower = now - timedelta(days=90)
        date_upper = now - timedelta(days=60)
        client_invoices = Invoice.objects.filter(invoice_client=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        # client_invoices_sum = client_invoices.aggregate(Sum('invoice_amount'))['invoice_amount__sum']
        # if client_invoices_sum == None:
        client_invoices_sum = 0
            
        client_payments = Receiving.objects.filter(receiving_client=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        client_payments_sum = client_payments.aggregate(Sum('receiving_amount'))['receiving_amount__sum']
        if client_payments_sum == None:
            client_payments_sum = 0

        payable_amount = client_invoices_sum - client_payments_sum
        return payable_amount

    def get_four_month(self):
        now=datetime.now()
        date_upper = now - timedelta(days=90)
        client_invoices = Invoice.objects.filter(invoice_client=self).filter(date_created__lte=date_upper)
        # client_invoices_sum = client_invoices.aggregate(Sum('invoice_amount'))['invoice_amount__sum']
        # if client_invoices_sum == None:
        client_invoices_sum = 0
            
        client_payments = Receiving.objects.filter(receiving_client=self).filter(date_created__lte=date_upper)
        client_payments_sum = client_payments.aggregate(Sum('receiving_amount'))['receiving_amount__sum']
        if client_payments_sum == None:
            client_payments_sum = 0

        payable_amount = client_invoices_sum - client_payments_sum
        return payable_amount

    def get_total(self):
        client_invoices = Invoice.objects.filter(invoice_client=self)
        #client_invoices_sum= client_invoices.aggregate(Sum('invoice_amount'))['invoice_amount__sum']

        # if client_invoices_sum == None:
        client_invoices_sum = 0

        client_payments = Receiving.objects.filter(receiving_client=self)
        client_payments_sum= client_payments.aggregate(Sum('receiving_amount'))['receiving_amount__sum']

        if client_payments_sum == None:
            client_payments_sum = 0

        payable_amount = client_invoices_sum - client_payments_sum
        return payable_amount

    def get_date(self):
        today = date.today()
        return today

    def __str__(self):
        return self.client_name


class Invoice(models.Model):

    CLIENT_ID_DEFAULT = None

    invoice_id = models.AutoField(primary_key=True)
    date_created=models.DateField()
    invoice_status = models.CharField(max_length=255)
    invoice_description=models.CharField(max_length=255, null=True)
    invoice_amount=models.IntegerField()
    invoice_client = models.ForeignKey(Client, on_delete=models.CASCADE,default=CLIENT_ID_DEFAULT,null=True)

    def invoice_get_amount(self):
        return none

    def __str__(self):
        return self.invoice_client.client_name + " | " 

class Invoice_Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    entry_service = models.ForeignKey(Service,on_delete=models.CASCADE)
    entry_invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    entry_qty = models.IntegerField()
    entry_rate = models.IntegerField()
    #1 id service, invoice no.1, 1 qty, 20$ 
    # 3 id service, invoice no.1, 2 qty, 30$
    
    def __str__(self):
        return self.entry_service.service_name #


class Receiving(models.Model):
    receiving_id=models.AutoField(primary_key=True)
    date_created = models.DateField()
    receiving_amount = models.IntegerField()
    receiving_description=models.CharField(max_length=255,null=True)
    receiving_client = models.ForeignKey(Client,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.receiving_client.client_name + " | " + str(self.receiving_amount)