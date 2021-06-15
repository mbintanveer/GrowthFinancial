from django.db import models
from django.db.models import Sum


class vendor(models.Model):
    vendorID=models.AutoField(primary_key=True)
    vendorName=models.CharField(max_length=50)
    vendorOwner=models.CharField(max_length=50)
    vendorCategory = models.CharField(max_length=50)
    vendorAmount = models.IntegerField()

    def __str__(self):
        return(self.vendorName + " - " +self.vendorCategory)

    def getAmount(self):

        from accountManagement.models import vendorExpense
        vendorExpenseList = vendorExpense.objects.filter(vendor=self).filter(expensePaid=False)
        vendorAmountSum = vendorExpenseList.aggregate(Sum('expenseAmount'))['expenseAmount__sum']

        if vendorAmountSum == None:
            vendorAmountSum = 0

        vendorAmount=vendorAmountSum

        return vendorAmount
