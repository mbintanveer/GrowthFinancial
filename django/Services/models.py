import os

from django.conf import settings
from django.db import models

class Service(models.Model):
    service_id=models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    service_price = models.IntegerField()

    def __str__(self):
        return self.service_name + " | " + str(self.service_price)

class Recurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    recurring_name=models.CharField(max_length=255)
    recurring_price=models.IntegerField()
    date_created=models.DateField()
    #Client Linkage in Recurring
    recurring_frequency = models.IntegerField()
    #recurring_unit Monthly Default For Now


    def __str__(self):
        return self.recurring_name + " | " + str(self.recurring_price)
        
class 