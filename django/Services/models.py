import os

from django.conf import settings
from django.db import models
 
class Service(models.Model):
    service_id=models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    service_price = models.IntegerField()
    service_default_qty=models.IntegerField(default=1)

    def __str__(self):
        return self.service_name + " | " + str(self.service_price)
    #     web development 20$/Hrs —> 3 Hrs default in a month. 
    # Graphic Designing 15$/Hrs —> 2 Hrs default in a month

class Recurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    recurring_name=models.CharField(max_length=255)
    recurring_price=models.IntegerField()
    date_created=models.DateField(null=True)
    #Client Linkage in Recurring
    recurring_frequency = models.IntegerField()
    #recurring_unit Monthly Default For Now


    def __str__(self):
        return self.recurring_name + " | " + str(self.recurring_price)
