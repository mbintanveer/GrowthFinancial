from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from accountManagement.models import generalExpense
from .models import invoice
from projectManagement.models import project
from accountManagement.decorators import top_level_required

#Pages
@login_required(login_url='/')
def iLanding(request):
    return render(request, 'iLanding.html')


@login_required(login_url='/')
@top_level_required(allowed_roles=['top_level'])
def iCompleted(request):

    invoicesCompleted = invoice.objects.filter(invoiceStatus="Completed")
    parameters = {'invoicesCompleted': invoicesCompleted}
    return render(request, 'iCompleted.html', parameters)


@login_required(login_url='/')
def iMgm(request):
     #--> CHange to pending
    invoicesOngoingSum = invoice.objects.filter(invoiceStatus="Ongoing")
    invoicesCompletedSum=invoice.objects.filter(invoiceStatus="Completed")
    parameters = {'invoicesOngoing': invoicesOngoingSum, 'invoicesCompleted': invoicesCompletedSum}

    return render(request, 'iMgm.html',parameters)


@login_required(login_url='/')
def iSpecific(request,id):
    currentInvoice = invoice.objects.get(pk=id)
    parameters = {'currentInvoice': currentInvoice}
    return render(request,'iSpecific.html',parameters)



@login_required(login_url='/')
def iEdit(request,id):
    from projectManagement.models import project
    from .models import typeOfInvoice
    currentInvoice = invoice.objects.get(pk=id)
    invoiceDate=currentInvoice.invoiceDate.strftime('%Y-%m-%d')

    projectRef = project.objects.exclude(projectName=currentInvoice.project.projectName)
    statusList=["Ongoing","Completed"]
    typeOfInvoice = typeOfInvoice.objects.exclude(typeName=currentInvoice.invoiceType)

    try:
        statusList.remove(currentInvoice.invoiceStatus)
    except:
        print("error")

    parameters = {'currentInvoice': currentInvoice, 'projectList': projectRef,
                    'statusList':statusList,'typeOfInvoice':typeOfInvoice,'invoiceDate':invoiceDate}
    return render(request, 'iEdit.html', parameters)

@login_required(login_url='/')
@top_level_required(allowed_roles=['top_level'])
def iSummary(request):
    from projectManagement.models import project,owner

    projectList = project.objects.all()
    ownerList=owner.objects.all()

    invoiceList=[]
    for project in projectList:
        invoiceList.append(invoice.objects.filter(project_id=project.projectID))

    invoiceListCompleted = invoice.objects.filter(invoiceStatus="Completed")
    invoiceListOngoing=invoice.objects.filter(invoiceStatus="Ongoing")

    invoiceCompletedSum =invoiceListCompleted.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']
    invoiceOngoingSum= invoiceListOngoing.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']

    #NONE TYPE CHECK
    if invoiceCompletedSum==None:
        invoiceCompletedSum =0

    if invoiceOngoingSum==None:
        invoiceOngoingSum=0

    invoiceCompletedSum/=1000000
    invoiceOngoingSum/=1000000

    parameters = {'invoiceList': invoiceList , 'projectList':projectList,'ownerList':ownerList,
                  'invoiceCompletedSum':invoiceCompletedSum,'invoiceOngoingSum':invoiceOngoingSum}

    return render(request,'iSummary.html',parameters)

@login_required(login_url='/')
def iAdd(request):
    from accountManagement.models import project
    from invoiceManagement.models import typeOfInvoice

    typeOfInvoice = typeOfInvoice.objects.all()

    projectList = project.objects.all()

    parameters = {'projectList': projectList,'typeOfInvoice':typeOfInvoice}

    return render(request,'iAdd.html',parameters)

#Functions

@login_required(login_url='/')
def editInvoiceFunction(request):
    invoiceID = request.POST.get('invoiceID')
    projectID = request.POST.get('projectID', 1)
    invoiceAmount = request.POST.get('invoiceAmount', '0')
    invoiceStatus = request.POST.get('invoiceStatus', 'Unknown')
    invoiceType = request.POST.get('invoiceType', '404')
    invoiceDate=request.POST.get('invoiceDate','01-02-2000')
    invoiceDetails = request.POST.get('invoiceDetails', 'No details found')
    invoiceAttachment = request.POST.get('invoiceAttachment')
    invoiceExtraWorkBoolean = request.POST.get('checkExtraWork', 'False')

    currentInvoice = invoice.objects.get(pk=invoiceID)
    currentInvoice.project = project.objects.get(pk=projectID)
    currentInvoice.invoiceAmount = invoiceAmount
    currentInvoice.invoiceStatus = invoiceStatus
    currentInvoice.invoiceType = invoiceType
    currentInvoice.invoiceDetails = invoiceDetails
    currentInvoice.invoiceDate=invoiceDate
    currentInvoice.invoiceAttachments = invoiceAttachment
    currentInvoice.invoiceExtraWorkBoolean = invoiceExtraWorkBoolean

    currentInvoice.save()

    redirectToinvoices = redirect('/invoiceManagement/iMgm')
    return redirectToinvoices

@login_required(login_url='/')
def addInvoiceFunction(request):

    from accountManagement.models import project
    from .models import invoice

    projectID = request.POST.get('projectID', 1)
    invoiceAmount = request.POST.get('invoiceAmount', '0')
    invoiceDate = request.POST.get('invoiceDate','01-02-2000')
    invoiceType=request.POST.get('invoiceType','404')
    invoiceDetails = request.POST.get('invoiceDetails', 'No Details Found')
    invoiceStatus=request.POST.get('invoiceStatus','Completed')
    invoiceAttachment = request.POST.get('invoiceAttachment', 'No Attachment Found')
    invoiceExtraWorkBoolean = request.POST.get('checkExtraWork', False)

    newObject = invoice.objects.create(
        project_id=projectID,
        invoiceAmount=invoiceAmount,
        invoiceDate=invoiceDate,
        invoiceType=invoiceType,
        invoiceDetails=invoiceDetails,
        invoiceStatus=invoiceStatus,
        invoiceAttachment=invoiceAttachment,
        invoiceExtraWorkBoolean=invoiceExtraWorkBoolean)

    from django.shortcuts import redirect
    response = redirect('/invoiceManagement/')
    return response


@login_required(login_url='/')
def removeInvoiceFunction(request, id):
    invoice.objects.filter(invoiceID=id).delete()
    redirectToInvoices = redirect('/invoiceManagement/iMgm')
    return redirectToInvoices



