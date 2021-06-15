import math
from sys import path

from django.db.models import Sum
from django.shortcuts import render, redirect
from accountManagement.models import generalExpense
from .models import project, owner
from invoiceManagement.models import invoice
from django.contrib.auth.decorators import login_required
from accountManagement.decorators import top_level_required
from accountManagement.models import vendorExpense,generalExpense

#Pages
@login_required(login_url="/")
def pLanding(request):
    return render(request, 'pLanding.html')


@login_required(login_url="/")
def pMgm(request):
    projectsOngoing = project.objects.filter(projectStatus="Ongoing")
    projectsCompleted=project.objects.filter(projectStatus="Completed")
    parameters = {'projectsOngoing': projectsOngoing,'projectsCompleted':projectsCompleted}
    return render(request, 'pMgm.html',parameters)


@login_required(login_url="/")
def pAdd(request):
    projects=project.objects.all()
    owners= owner.objects.all()

    parameters = {'projectList':projects, 'ownerList' : owners}
    return render(request,'pAdd.html',parameters)


@login_required(login_url="/")
@top_level_required(allowed_roles=['top_level'])
def pSummary(request):

    from .models import project
    project = project.objects.all()
    sumValueProjects = math.floor((project.aggregate(Sum('projectValue'))['projectValue__sum'])/1000000)

    parameters = {'projects': project,
                  'sumProjects_inhand': sumValueProjects,
                  }

    return render(request,'pSummary.html',parameters)


@login_required(login_url="/")
@top_level_required(allowed_roles=['top_level']) 
def pSpecific(request,id):

    generalExpenseList=generalExpense.objects.filter(project_id=id)
    invoiceList=invoice.objects.filter(project_id=id)
    projectObject = project.objects.filter(projectID=id)
    invoiceCompletedList= invoiceList.filter(invoiceStatus="Completed")
    invoiceOngoingList=invoiceList.filter(invoiceStatus="Ongoing")
    projectValue = projectObject.aggregate(Sum('projectValue'))['projectValue__sum']
    invoiceCompletedSum =invoiceCompletedList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum'] #Lac Conversion
    invoiceOngoingSum = invoiceOngoingList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']
    generalExpenseSum = generalExpenseList.aggregate(Sum('expenseAmount'))['expenseAmount__sum']


    if invoiceCompletedSum==None:
        invoiceCompletedSum=0
    if invoiceOngoingSum==None:
        invoiceOngoingSum=0
    if generalExpenseSum == None:
        generalExpenseSum = 0


        #Lac Conversion
    projectValue=projectValue/ 1000000
    invoiceCompletedSum=invoiceCompletedSum/1000000
    invoiceOngoingSum=invoiceOngoingSum/1000000
    generalExpenseSum =generalExpenseSum/ 1000000
    expenseSum = generalExpenseSum 
    invoiceSum = invoiceCompletedSum + invoiceOngoingSum
    projectProfit=invoiceCompletedSum - generalExpenseSum 
    projectRemainingSum=projectValue - invoiceSum

    parameters = {'projectList': projectObject,
                  'expenseSum':expenseSum,
                  'invoiceListOngoing':invoiceOngoingList,
                  'invoiceListCompleted':invoiceCompletedList,
                  'generalExpenseList': generalExpenseList,
                  'projectValue':round(projectValue,2),
                  'invoiceOngoingSum': round(invoiceOngoingSum,2),
                  'invoiceCompletedSum': round(invoiceCompletedSum,2),
                  'generalExpenseSum': round(generalExpenseSum,2),
                  'invoiceSum': round(invoiceSum,2),
                  'projectRemainingSum': round(projectRemainingSum,2),
                    'projectProfit':round(projectProfit,2),
                  }
    return render(request, 'pSpecific.html', parameters)


@login_required(login_url="/")
def pEdit(request,id):
    currentProject = project.objects.get(pk=id)
    projects = project.objects.exclude(projectName=currentProject.projectName)
    owners = owner.objects.exclude(ownerName=currentProject.projectOwner)
    status = ["Ongoing","Completed"]
    try:
        status.remove(currentProject.projectStatus)
    except:
        print("error")

    parameters = {'currentProject':currentProject,'projectList': projects, 'ownerList': owners,
                  'statusRef': status}

    return render(request, 'pEdit.html',parameters)


#Functions

@login_required(login_url="/")
def addProjectFunction(request):
    projectName = request.POST.get('projectName')
    projectOwner = request.POST.get('projectOwner')
    projectValue=request.POST.get('projectValue')
    projectStatus=request.POST.get('projectStatus')


    currentProject = project.objects.create(projectName=projectName, projectOwner=projectOwner
                                        , projectValue=projectValue,projectStatus=projectStatus)

    redirectToProjects = redirect('/projectManagement/pMgm')
    return redirectToProjects

@login_required(login_url="/")
def editProjectFunction(request):
    projectID=request.POST.get('projectID')
    projectName = request.POST.get('projectName')
    projectOwner = request.POST.get('projectOwner')
    projectValue=request.POST.get('projectValue')

    projectStatus=request.POST.get('projectStatus')

    currentProject = project.objects.get(pk=projectID)
    currentProject.projectName=projectName
    currentProject.projectOwner=projectOwner
    currentProject.projectValue = projectValue

    currentProject.projectStatus = projectStatus
    currentProject.save()

    redirectToProjects = redirect('/projectManagement/pMgm')
    return redirectToProjects