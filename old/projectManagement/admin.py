from django.contrib import admin

# Register your models here.
from .models import project,owner


admin.site.register(project)
admin.site.register(owner)