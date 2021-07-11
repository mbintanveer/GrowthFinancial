from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .serializers import ExpenseSerializer
from rest_framework.decorators import api_view

from .models import Expense

def Expenses_Landing(request):
    return render(request,'Expenses_Landing.html')

@api_view(['GET', 'POST', 'DELETE'])
def expense_list(request):
    if request.method == 'GET':
        Expense = Expense.objects.all()
        expense_serializer = ExpenseSerializer(Expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)

    elif request.method == 'POST':
        expense_data = JSONParser().parse(request)
        expense_serializer =ExpenseSerializer(data=expense_data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return JsonResponse(expense_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def expense_detail(request, pk):  
    try: 
        expense = Expense.objects.get(pk=pk) 
        if request.method == 'GET': 
            expense_serializer = ExpenseSerializer(expense) 
        return JsonResponse(expense_serializer.data) 
    except Expense.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
