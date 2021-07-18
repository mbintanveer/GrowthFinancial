from rest_framework import serializers
from Vendors.models import Payments, Vendors, Bills

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ('vendor_id',
                'vendor_name',
               )

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('bill_id',
                'date_created',
                'bill_amount',
                'bill_description',
                'bill_vendor')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('payment_id',
                'date_created',
                'payment_amount',
                'payment_description',
                'payment_vendor')

