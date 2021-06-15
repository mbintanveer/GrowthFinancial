from django import http
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect



def index(request):
    return render(request,'index.html')




def signIn(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password = password)

        if user is not None:
            login(request,user)
            print("Correct")
            index = redirect('/')
            return index

        else:

            messages.info(request,"Username or Password is incorrect")
            print("Incorrect")
            index = redirect('/')
            return index

def signOut(request):
    logout(request)
    index = redirect('/')
    return index


def unavailable(request):
    return render(request,'unavailable.html')