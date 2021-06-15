import os

from django.conf import settings
from django.db import models


from projectManagement.models import project
from vendorManagement.models import vendor


#Expense Models
class generalExpense(models.Model):
  
    expenseID = models.AutoField(primary_key=True)
    project=models.ForeignKey (project,on_delete=models.CASCADE,related_name='generalExpenseProject')
    expenseDate = models.DateField()
    expenseReceipient = models.CharField(max_length=50,default="Not Found")
    expenseAmount = models.IntegerField()
    #expenseDetails = models.TextField()

    def generalExpense_path(self):
        return os.path.join(settings.LOCAL_FILE_DIR, 'generalExpense/%Y/%m/')

    def __str__(self):
        return (self.project.projectName + " - " + str(self.expenseAmount))


class vendorExpense(models.Model):


    expenseID = models.AutoField(primary_key=True)
    expenseDate = models.DateField()
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE,related_name='vendor')
    expenseType = models.CharField(max_length=50,default="")
    expenseAmount = models.IntegerField()
    expensePaid=models.BooleanField(default = True)

    def vendorExpense_path(self):
        return os.path.join(settings.LOCAL_FILE_DIR, 'vendorExpense/%Y/%m/')

    def __str__(self):
        return (  str(self.expenseAmount) + "| Details:  " + self.expenseDetails + " "+ str(self.expenseExtraWorkBoolean))

    def shortSummary(self):
        return(self.expenseType + self.expenseDetails)


