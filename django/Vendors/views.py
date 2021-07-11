
from django.shortcuts import render
from .models import Vendors, Bills, Payments
from itertools import chain
from operator import attrgetter

Bills = Bills.objects.all()

def Vendors_Landing(request):
    VendorsList = Vendors.objects.all()
    params = {'VendorsList':VendorsList}
    
    return render(request,'Vendors_Landing.html',params)

def Vendors_View(request,id):
    from .models import Bills, Payments

    vendor =  Vendors.objects.get(pk=id)
    Bills=Bills.objects.filter(bill_vendor=vendor)
    Payments = Payments.objects.filter(payment_vendor=vendor)
    combined_results = sorted(
    chain(Bills, Payments),
    key=attrgetter('date_created'),reverse=True)

    params= {'vendor':vendor,'combined_results':combined_results}

    return render(request,'Vendors_View.html',params)

@api_view(['GET','POST'])
def expenses_list(request):
    if request.method == 'GET':
        expense = Expense.objects.all()
        expense_serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(expense_serializer.data, safe=False)

    elif request.method == 'POST':
        expense_data = JSONParser().parse(request)
        expense_serializer =ExpenseSerializer(data=expense_data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return JsonResponse(expense_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def expenses_detail(request, pk):  
    try: 
        expense = Expense.objects.get(pk=pk) 
    except Expense.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        expense_serializer = ExpenseSerializer(expense) 
        return JsonResponse(expense_serializer.data) 

    elif request.method == 'PUT': 
        expense_data = JSONParser().parse(request) 
        expense_serializer = ExpenseSerializer(expense, data=expense_data) 
        if expense_serializer.is_valid(): 
            expense_serializer.save() 
            return JsonResponse(expense_serializer.data) 
        return JsonResponse(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        expense.delete() 
        return JsonResponse({'message': 'Invoice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        