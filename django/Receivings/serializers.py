from rest_framework import serializers
from Clients.models import Receiving

class ReceivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiving
        fields = ('receiving_id',
                'date_created',
                'receiving_amount',
               'receiving_description',
                'receiving_client')
   
               

