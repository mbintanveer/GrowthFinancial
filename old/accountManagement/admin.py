from django.contrib import admin

# Register your models here.

from .models import generalExpense,vendorExpense

admin.site.register(generalExpense)
admin.site.register(vendorExpense)
