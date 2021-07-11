from rest_framework import serializers
from Vendors.models import Vendors

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ('vendor_id',
                'vendor_name',
               )

