from django.shortcuts import render
# from .serializers import ServiceSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def Services_Landing(request):
    return render(request,'Services_Landing.html')

def Services_Add(request):

    return render(request,'Services_Add.html')

def Recurring_Add(request):

   return render(request,'Recurring_Add.html')


# @api_view(['GET','POST'])
# def services_list(request):
#     if request.method == 'GET':
#         expense = Expense.objects.all()
#         expense_serializer = ExpenseSerializer(expense, many=True)
#         return JsonResponse(expense_serializer.data, safe=False)

#     elif request.method == 'POST':
#         expense_data = JSONParser().parse(request)
#         expense_serializer =ExpenseSerializer(data=expense_data)
#         if expense_serializer.is_valid():
#             expense_serializer.save()
#             return JsonResponse(expense_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def services_detail(request, pk):  
#     try: 
#         expense = Expense.objects.get(pk=pk) 
#     except Expense.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
#     if request.method == 'GET': 
#         expense_serializer = ExpenseSerializer(expense) 
#         return JsonResponse(expense_serializer.data) 

#     elif request.method == 'PUT': 
#         expense_data = JSONParser().parse(request) 
#         expense_serializer = ExpenseSerializer(expense, data=expense_data) 
#         if expense_serializer.is_valid(): 
#             expense_serializer.save() 
#             return JsonResponse(expense_serializer.data) 
#         return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#     elif request.method == 'DELETE': 
#         expense.delete() 
#         return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        