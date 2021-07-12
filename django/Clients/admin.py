from django.contrib import admin
from .models import Client,Invoice,Receiving,Invoice_Entry

# Register your models here.
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Receiving)
admin.site.register(Invoice_Entry)
