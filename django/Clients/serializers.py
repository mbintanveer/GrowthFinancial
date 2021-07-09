from rest_framework import serializers
from Clients.models import Client,Receiving

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'client_name')

class ReceivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiving
        fields = ('receiving_id',
                'date_created',
                'receiving_amount',
                'receiving_description',
                'receiving_client')