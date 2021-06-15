import os

from django.conf import settings
from django.db import models
from projectManagement.models import project


class invoice(models.Model):

    invoiceID = models.AutoField(primary_key=True)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    invoiceAmount = models.IntegerField()
    invoiceType = models.CharField(max_length=50, default="")
    invoiceDate = models.DateField()
    invoiceStatus=models.CharField(max_length=50,default="paid")


    def desc(self):
        return (self.project.projectName+" | " +str(self.invoiceAmount/1000000) + " | " + self.invoiceType+ " | " )
    def invoice_path(self):
        return os.path.join(settings.LOCAL_FILE_DIR, 'generalExpense/%Y/%m/')


