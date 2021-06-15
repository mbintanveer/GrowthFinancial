import datetime
import os
from django.conf import settings
from django.db import models
from django.db.models import Sum
from tryTwo.settings import BASE_DIR


class project(models.Model):
    completed = 'Completed'
    ongoing = 'Ongoing'
    projectStatusChoices = [
        (completed, 'Completed'),
        (ongoing, 'Ongoing'),
    ]


    projectID=models.AutoField(primary_key=True)
    projectName=models.CharField(max_length=60)
    projectOwner=models.CharField(max_length=40)
    projectValue=models.IntegerField(default=1)
    projectStatus = models.CharField(max_length=20,choices=projectStatusChoices,default=completed)
    projectImage = models.FilePathField(path=os.path.join(settings.BASE_DIR, 'media/projects'),default="File not uploaded at entry",blank=True)

    def __str__(self):
        return(self.projectName + " - Project Of: " + self.projectOwner)

    def editProject(self,pid,projectInstance):
        sample = self.objects.get(pk=pid)
        sample = projectInstance
        sample.save()

    def shortSummary(self):
        return(self.projectName + " - OWNER:  " + self.projectOwner)

    def projectInvoiceOngoingSum(self):
        from invoiceManagement.models import invoice
        invoiceList=invoice.objects.filter(project=self).filter(invoiceStatus="Ongoing")
        sumInvoicePending = invoiceList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']
        if sumInvoicePending == None:
            sumInvoicePending = 0

        sumInvoicePending = sumInvoicePending / 1000000
        return sumInvoicePending

    def projectInvoiceCompletedSum(self):
        from invoiceManagement.models import invoice
        invoiceList=invoice.objects.filter(project=self).filter(invoiceStatus="Completed")
        sumInvoiceOngoing =invoiceList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']
        if sumInvoiceOngoing == None:
            sumInvoiceOngoing=0
        sumInvoiceOngoing=sumInvoiceOngoing/1000000
        return sumInvoiceOngoing


    def projectMonthlySum(self):
        from invoiceManagement.models import invoice

        currentMonth = datetime.datetime.now().month

        invoiceList=invoice.objects.filter(project=self).filter(invoiceStatus="Completed").filter(invoiceDate__month = currentMonth)
        sumInvoiceOngoing =invoiceList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']
        if sumInvoiceOngoing == None:
            sumInvoiceOngoing=0
        sumInvoiceOngoing=sumInvoiceOngoing/1000000
        return sumInvoiceOngoing


    def getProjectValue(self):
        return (self.projectValue)

class owner(models.Model):
    ownerID = models.AutoField(primary_key=True)
    ownerName = models.TextField(max_length=50)
    ownerReference=models.TextField(max_length=50)

    def __str__(self):
        return self.ownerName


