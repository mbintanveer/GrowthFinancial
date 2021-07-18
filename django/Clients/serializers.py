from rest_framework import serializers
from Clients.models import Client,Receiving,Invoice

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'client_name')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('invoice_id',
                'date_created',
                # 'invoice_amount',
                'invoice_description',
                'invoice_client')

class ReceivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiving
        fields = ('receiving_id',
                'date_created',
                'receiving_amount',
                'receiving_description',
                'receiving_client')

