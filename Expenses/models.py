
from django.db import models

class Expense(models.Model):
    expense_id=models.AutoField(primary_key=True)
    expense_amount = models.IntegerField()

    type_choices = (
        ('Marketing','Marketing')
        ,('Payroll', 'Payroll' ))

    expense_type = models.CharField(max_length=255, choices=type_choices)
    expense_date = models.DateField()


    def __str__(self):
        return self.expense_type + " | " + self.expense_amount

