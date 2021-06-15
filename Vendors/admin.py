from django.contrib import admin

# Register your models here.

from .models import Vendors,Bills,Payments

admin.site.register(Vendors)
admin.site.register(Bills)
admin.site.register(Payments)
