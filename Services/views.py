from django.shortcuts import render

# Create your views here.
def Services_Landing(request):
    return render(request,'Services_Landing.html')

def Services_Add(request):

    return render(request,'Services_Add.html')

def Recurring_Add(request):

   return render(request,'Recurring_Add.html')