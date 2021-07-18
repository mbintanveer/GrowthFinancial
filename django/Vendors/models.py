import os
from django.db import models
from django.db.models import Sum
import datetime
from datetime import date,datetime
from datetime import timedelta

class Vendors(models.Model):
    vendor_id=models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.vendor_name 

    def get_one_month(self): #NO UPPER BOUND AS WE GET > 30 Days
        now = datetime.now()
        date_lower = now - timedelta(days=30)

        vendor_bills = Bills.objects.filter(bill_vendor=self).filter(date_created__gte=date_lower)
        vendor_bills_sum = vendor_bills.aggregate(Sum('bill_amount'))['bill_amount__sum']
        if vendor_bills_sum == None:
            vendor_bills_sum = 0

        vendor_payments = Payments.objects.filter(payment_vendor=self).filter(date_created__gte=date_lower)
        vendor_payments_sum = vendor_payments.aggregate(Sum('payment_amount'))['payment_amount__sum']
        if vendor_payments_sum == None:
            vendor_payments_sum = 0
        payable_amount = vendor_bills_sum - vendor_payments_sum
        return payable_amount

    def get_two_month(self):
        now = datetime.now()
        date_lower = now - timedelta(days=60)
        date_upper = now - timedelta(days=30)

        vendor_bills = Bills.objects.filter(bill_vendor=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        vendor_bills_sum = vendor_bills.aggregate(Sum('bill_amount'))['bill_amount__sum']
        if vendor_bills_sum == None:
            vendor_bills_sum = 0

        vendor_payments = Payments.objects.filter(payment_vendor=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        vendor_payments_sum = vendor_payments.aggregate(Sum('payment_amount'))['payment_amount__sum']
        if vendor_payments_sum == None:
            vendor_payments_sum = 0

        payable_amount = vendor_bills_sum - vendor_payments_sum
        return payable_amount

    def get_three_month(self):
        now=datetime.now()
        date_lower = now - timedelta(days=90)
        date_upper = now - timedelta(days=60)
        vendor_bills = Bills.objects.filter(bill_vendor=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        vendor_bills_sum = vendor_bills.aggregate(Sum('bill_amount'))['bill_amount__sum']
        if vendor_bills_sum == None:
            vendor_bills_sum = 0
            
        vendor_payments = Payments.objects.filter(payment_vendor=self).filter(date_created__gte=date_lower, 
        date_created__lte=date_upper)
        vendor_payments_sum = vendor_payments.aggregate(Sum('payment_amount'))['payment_amount__sum']
        if vendor_payments_sum == None:
            vendor_payments_sum = 0

        payable_amount = vendor_bills_sum - vendor_payments_sum
        return payable_amount

    def get_four_month(self):
        now=datetime.now()
        date_upper = now - timedelta(days=90)
        vendor_bills = Bills.objects.filter(bill_vendor=self).filter(date_created__lte=date_upper)
        vendor_bills_sum = vendor_bills.aggregate(Sum('bill_amount'))['bill_amount__sum']
        if vendor_bills_sum == None:
            vendor_bills_sum = 0
            
        vendor_payments = Payments.objects.filter(payment_vendor=self).filter(date_created__lte=date_upper)
        vendor_payments_sum = vendor_payments.aggregate(Sum('payment_amount'))['payment_amount__sum']
        if vendor_payments_sum == None:
            vendor_payments_sum = 0

        payable_amount = vendor_bills_sum - vendor_payments_sum
        return payable_amount

    def get_total(self):
        vendor_bills = Bills.objects.filter(bill_vendor=self)
        vendor_bills_sum= vendor_bills.aggregate(Sum('bill_amount'))['bill_amount__sum']

        if vendor_bills_sum == None:
            vendor_bills_sum = 0

        vendor_payments = Payments.objects.filter(payment_vendor=self)
        vendor_payments_sum= vendor_payments.aggregate(Sum('payment_amount'))['payment_amount__sum']

        if vendor_payments_sum == None:
            vendor_payments_sum = 0

        payable_amount = vendor_bills_sum - vendor_payments_sum
        return payable_amount

    def get_date(self):
        today = date.today()
        return today


class Bills(models.Model):
    bill_id=models.AutoField(primary_key=True,blank=True)
    bill_vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE,related_name='bill_vendor')
    bill_description = models.CharField(max_length=255)
    bill_amount = models.IntegerField()
    date_created = models.DateField(null=True)
    def __str__(self):
        return (self.bill_vendor.__str__() + " | " + str(self.bill_amount))

class Payments(models.Model):
    payment_id=models.AutoField(primary_key=True,blank=True)
    payment_vendor=models.ForeignKey(Vendors,on_delete=models.CASCADE,related_name='payment_vendor')
    payment_description=models.CharField(max_length=255)
    payment_amount = models.IntegerField()
    date_created = models.DateField(null=True)

    def __str__(self):
        return self.payment_vendor.__str__() + " | " + str(self.payment_amount)
