from django.shortcuts import render
from rest_framework.decorators import api_view
from Clients.models import Receiving
from .serializers import ReceivingSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def Receivings_Landing(request):
    return render(request,'Receivings_Landing.html')

@api_view(['GET','POST'])
def receivings_list(request):
    if request.method == 'GET':
        receiving = Receiving.objects.all()
        receiving_serializer = ReceivingSerializer(receiving, many=True)
        return JsonResponse(receiving_serializer.data, safe=False)

    elif request.method == 'POST':
        receiving_data = JSONParser().parse(request)
        receiving_serializer =ReceivingSerializer(data=receiving_data)
        if receiving_serializer.is_valid():
            receiving_serializer.save()
            return JsonResponse(receiving_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(receiving_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def receivings_detail(request, pk):  
    try: 
        receiving = Receiving.objects.get(pk=pk) 
    except Receiving.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        receiving_serializer = ReceivingSerializer(receiving) 
        return JsonResponse(receiving_serializer.data) 

    elif request.method == 'PUT': 
        receiving_data = JSONParser().parse(request) 
        receiving_serializer = ReceivingSerializer(receiving, data=receiving_data) 
        if receiving_serializer.is_valid(): 
            receiving_serializer.save() 
            return JsonResponse(receiving_serializer.data) 
        return JsonResponse(receiving_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        receiving.delete() 
        return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        