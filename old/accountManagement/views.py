import calendar
import datetime

from django import http
from django.db.models import Sum
from django.shortcuts import render, redirect
from accountManagement.models import generalExpense, vendorExpense, vendor
from projectManagement.models import project
from django.contrib.auth.decorators import login_required
from .decorators import top_level_required, auth_required


@login_required(login_url="/")
def aLanding(request):
    return render(request, 'aLanding.html')


@login_required(login_url='/')
def aMgm(request):
    from accountManagement.models import generalExpense, vendorExpense

    generalExpenseList= generalExpense.objects.all()
    vendorExpenseList=vendorExpense.objects.filter(expensePaid=False)
    parameters = {'generalExpenseList':generalExpenseList,
                  'vendorExpenseList':vendorExpenseList,
                  }

    return render(request,'aMgm.html',parameters)


@login_required(login_url='/')
@top_level_required(allowed_roles=['top_level'])
def aSummary(request):
    from invoiceManagement.models import invoice
    projectList=project.objects.all()
    currentMonth = datetime.datetime.now().month
    generalExpenseList = generalExpense.objects.all().filter(expenseDate__month=currentMonth)
    vendorExpenseList = vendorExpense.objects.all().filter(expenseDate__month=currentMonth)

    facilitiesList = generalExpenseList.filter(expenseType="Facilities")
    labourAdminList =generalExpenseList.filter(expenseType="Labour Admin")
    marketingList=generalExpenseList.filter(expenseType="Marketing")
    otherExpensesList=generalExpenseList.filter(expenseType="Other Expenses")


    invoiceCompletedSumList = invoice.objects.filter(invoiceDate__month = currentMonth).filter(invoiceStatus="Completed")
    invoiceCompletedSum = invoiceCompletedSumList.aggregate(Sum('invoiceAmount'))['invoiceAmount__sum']

    if invoiceCompletedSum==None:
        invoiceCompletedSum=0

    generalMaterial = generalExpenseList.filter(expenseType="Material").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    generalVendor = vendorExpenseList.filter(expenseType="Material").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    if generalMaterial==None:
        generalMaterial =0

    if generalVendor ==None:
        generalVendor =0

    sumMaterial= generalMaterial + generalVendor

    if sumMaterial==None:
        sumMaterial=0

    generalSiteLabour = generalExpenseList.filter(expenseType="Site Labour").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    vendorSiteLabour = vendorExpenseList.filter(expenseType ="Site Labour").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    if generalSiteLabour ==None:
        generalSiteLabour = 0

    if vendorSiteLabour ==None:
        vendorSiteLabour = 0


    sumSiteLabour = generalSiteLabour + vendorSiteLabour

    if sumSiteLabour == None:
        sumSiteLabour = 0

    generalMaterialAndLabour = generalExpenseList.filter(expenseType="Material and Labour").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']
    vendorMaterialAndLabour = vendorExpenseList.filter(expenseType="Material and Labour").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']
    if generalMaterialAndLabour ==None:
        generalMaterialAndLabour = 0

    if vendorMaterialAndLabour ==None:
        vendorMaterialAndLabour =0

    sumMaterialAndLabour = generalMaterialAndLabour + vendorMaterialAndLabour

    if sumMaterialAndLabour == None:
        sumMaterialAndLabour = 0

    generalAdvance = generalExpenseList.filter(expenseType="Advance").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']
    vendorAdvance = vendorExpenseList.filter(expenseType="Advance").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']
    if generalAdvance ==None:
        generalAdvance = 0

    if vendorAdvance ==None:
        vendorAdvance = 0

    sumAdvance =generalAdvance + vendorAdvance

    if sumAdvance == None:
        sumAdvance = 0

    costOfProjectSum = sumAdvance + sumMaterial + sumMaterialAndLabour + sumSiteLabour
    grossProfit = invoiceCompletedSum - costOfProjectSum
    if grossProfit ==None:
        grossProfit=0

    generalMarketing = generalExpenseList.filter(expenseType="Marketing").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    vendorMarketing= vendorExpenseList.filter(expenseType="Marketing").aggregate(Sum('expenseAmount'))['expenseAmount__sum']
    if generalMarketing ==None:
        generalMarketing = 0

    if vendorMarketing ==None:
        vendorMarketing = 0

    sumMarketing = generalMarketing + vendorMarketing

    if sumMarketing == None:
        sumMarketing = 0

    generalFacilities = generalExpenseList.filter(expenseType="Facilities").aggregate(Sum('expenseAmount'))[ 'expenseAmount__sum']
    vendorFacilities = vendorExpenseList.filter(expenseType = "Facilities").aggregate(Sum('expenseAmount'))[ 'expenseAmount__sum']

    if generalFacilities == None:
        generalFacilities = 0

    if vendorFacilities ==None:
        vendorFacilities= 0

    sumFacilities = generalFacilities + vendorFacilities

    if sumFacilities == None:
        sumFacilities = 0

    generalOtherExpenses = generalExpenseList.filter(expenseType="Other Expenses").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']
    vendorOtherExpenses = vendorExpenseList.filter(expenseType="Other Expenses").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']

    if generalOtherExpenses ==None:
        generalOtherExpenses = 0

    if vendorOtherExpenses ==None:
        vendorOtherExpenses=0

    sumOtherExpenses = generalOtherExpenses + vendorOtherExpenses

    if sumOtherExpenses == None:
        sumOtherExpenses = 0

    generalAdminLabour =  generalExpenseList.filter(expenseType="Admin Labour").aggregate(Sum('expenseAmount'))[
        'expenseAmount__sum']

    sumAdminLabour = generalAdminLabour

    if sumAdminLabour == None:
        sumAdminLabour = 0


    invoiceCompletedSum=round((invoiceCompletedSum/1000000),2) #To Million
    costOfProjectSum=round((costOfProjectSum/100000),2)
    netIncome = grossProfit - sumFacilities - sumMarketing - sumAdminLabour - sumOtherExpenses
    grossProfit=round((grossProfit/100000),2)
    sumAdminLabour=round((sumAdminLabour/100000),2)
    sumMarketing=round((sumMarketing/1000),2)
    sumOtherExpenses=round((sumOtherExpenses/1000),2)
    sumFacilities=round((sumFacilities/100000),2)
    netIncome=round((netIncome/100000),2)

    parameters ={'projectList':projectList,'invoiceCompletedSum':invoiceCompletedSum,'costOfProjectSum':costOfProjectSum,
                 'grossProfit':grossProfit,'sumAdminLabour':sumAdminLabour,'sumMarketing':sumMarketing,
                 'sumOtherExpenses':sumOtherExpenses,'sumFacilities':sumFacilities,'facilitiesList':facilitiesList,
                 'labourAdminList':labourAdminList, 'marketingList':marketingList,'otherExpensesList':otherExpensesList,
                 'netIncome':netIncome,'currentMonth':calendar.month_name[currentMonth]}

    return render(request,'aSummary.html',parameters)



@login_required(login_url="/")
def addGeneralExpense(request):
    from invoiceManagement.models import invoice
    from projectManagement.models import project

    projectList = project.objects.all()
    vendorList=vendor.objects.all()

    parameters= {'projectList': projectList,'vendorList':vendorList,}
    return render(request,'aGeneralExpenseAdd.html', parameters)


@login_required(login_url="/")
def addVendorExpense(request):
    from invoiceManagement.models import invoice
    from projectManagement.models import project

    projectList = project.objects.all()
    vendorList=vendor.objects.all()

    parameters = {'projectList': projectList, 'vendorList': vendorList, }
    return render(request, 'aVendorExpenseAdd.html', parameters)


@login_required(login_url="/")
def allVendorExpense(request):

    vendorExpenseList=vendorExpense.objects.all()
    parameters={'vendorExpenseList':vendorExpenseList}

    return render(request,'aVendorExpenseAll.html',parameters)


@login_required(login_url="/")
def allGeneralExpense(request):
    generalExpenseList = generalExpense.objects.all()
    parameters = {'generalExpenseList': generalExpenseList}

    return render(request, 'aGeneralExpenseAll.html', parameters)

#FUNCTIONS

#@login_required(login_url="/")
def addGeneralExpenseFunction(request):

    from accountManagement.models import generalExpense
    from invoiceManagement.models import invoice

    projects = project.objects.all()
    projectID = request.POST.get('projectID',0)
    expenseAmount = request.POST.get('expenseAmount', '0')
    expenseDate = request.POST.get('expenseDate','01-02-2000')
    expenseDetails = request.POST.get('expenseDetails', 'No Details Found')
    expenseReceipient=request.POST.get('expenseReceipient','Unknown')
    expenseAttachment = request.POST.get('expenseAttachment', 'No Attachment Found')
    expenseExtraWorkBoolean = request.POST.get('checkExtraWork',False)
    expenseType=request.POST.get('expenseType','Not Found')
    currentProject = project.objects.get(pk = projectID)
    #BUG

    newObject = generalExpense.objects.create(
    project=currentProject,
    expenseAmount=expenseAmount,
    expenseDate=expenseDate,
    expenseDetails=expenseDetails,
    expenseReceipient=expenseReceipient,
    expenseAttachment=expenseAttachment,
    expenseType=expenseType,
    expenseExtraWorkBoolean=expenseExtraWorkBoolean)

    redirectToManagement = redirect('/accountManagement/aMgm')
    return redirectToManagement


@login_required(login_url="/")
def addVendorExpenseFunction(request):
    from projectManagement.models import project
    from accountManagement.models import vendorExpense
    from invoiceManagement.models import invoice
    from vendorManagement.models import vendor

    projects = project.objects.all()
    projectID = request.POST.get('projectID',0)
    expenseAmount = request.POST.get('expenseAmount', '0')
    expenseDate = request.POST.get('expenseDate','2000-01-01')
    expenseDetails = request.POST.get('expenseDetails', 'No Details Found')
    expenseAttachment = request.POST.get('expenseAttachment', 'No Attachment Found')
    expenseExtraWorkBoolean = request.POST.get('checkExtraWork',False)
    expenseType=request.POST.get('expenseType','Not Found')
    expensePaid = request.POST.get('expensePaid',False)
    projectInput = project.objects.get(pk = projectID)
    vendorID = request.POST.get('vendorID',0)
    vendorInput = vendor.objects.get(pk=vendorID)

    #BUG
    if expensePaid=="True":
        bol=True
    else:
        bol = False

    if (bol == False):
        vendorInput.vendorAmount += int(expenseAmount)
        vendorInput.save()

    newObject = vendorExpense.objects.create(
    project=projectInput,
    expenseAmount=expenseAmount,
    expenseDate=expenseDate,
    expenseDetails=expenseDetails,
    expenseAttachment=expenseAttachment,
    expenseType=expenseType,
    expenseExtraWorkBoolean=expenseExtraWorkBoolean,
    vendor=vendorInput,
    expensePaid = bol,
    )


    redirectToManagement = redirect('/accountManagement/aMgm')
    return redirectToManagement


@login_required(login_url="/")
def editGeneralExpense(request,primaryKey):
    from accountManagement.models import generalExpense
    from projectManagement.models import project
    from accountManagement.models import vendor

    try:
        currentExpense = generalExpense.objects.get(pk=primaryKey)
        projectList = project.objects.exclude(projectName=currentExpense.project.projectName)
        vendorRef = vendor.objects.exclude(vendorName=currentExpense.vendor.vendorName)
    except:
        currentExpense=generalExpense.objects.get(pk=primaryKey)
        projectList=None
        vendorRef=None

    typeOfExpense = ["Site Labour",
                     "Material",
                     "Material And Labour", "Advance",
                     "Admin Labour", "Marketing", "Facilities", "Other Expenses"]

    try:
        typeOfExpense.remove(currentExpense.expenseType)

    except:
        print("Error")

    expenseDate = currentExpense.expenseDate.strftime('%Y-%m-%d')
    parameters = {'currentExpense': currentExpense, 'projectList': projectList,
                    'vendorRef':vendorRef,'typeOfExpense':typeOfExpense,'expenseDate':expenseDate}
    return render(request, 'aEditGeneral.html', parameters)

@login_required(login_url="/")
def editVendorExpense(request,primaryKey):
    from accountManagement.models import vendorExpense
    from projectManagement.models import project
    from accountManagement.models import vendor

    try:
        currentExpense = vendorExpense.objects.get(pk=primaryKey)
        projectList = project.objects.exclude(projectName=currentExpense.project.projectName)
        vendorRef = vendor.objects.exclude(vendorName=currentExpense.vendor.vendorName)
    except:
        currentExpense=generalExpense.objects.get(pk=primaryKey)
        projectList=None
        vendorRef=None
    typeOfExpense = ["Site Labour",
                     "Material",
                     "Material And Labour", "Advance",
                     "Admin Labour", "Marketing", "Facilities", "Other Expenses"]
    try:
        typeOfExpense.remove(currentExpense.expenseType)

    except:
        print("Error")

    expenseDate = currentExpense.expenseDate.strftime('%Y-%m-%d')
    parameters = {'currentExpense': currentExpense, 'projectList': projectList,
                    'vendorRef':vendorRef,'typeOfExpense':typeOfExpense,
                  'expenseDate':expenseDate}

    return render(request, 'aEditVendor.html', parameters)

@login_required(login_url="/")
def viewGeneralExpense(request,id):
    currentExpense = generalExpense.objects.get(pk=id)
    parameters= {'currentExpense':currentExpense}
    return render(request,'aGeneralExpenseSpecific.html',parameters)


@login_required(login_url="/")
def viewVendorExpense(request,id):
    from .models import vendorExpense
    vendorExpense = vendorExpense.objects.get(pk=id)
    parameters = {'currentExpense': vendorExpense}
    return render(request, 'aVendorExpenseSpecific.html', parameters)


@login_required(login_url="/")
def editVendorExpenseFunction(request):
    from accountManagement.models import vendorExpense

    expenseID = request.POST.get('expenseID')
    projectID = request.POST.get('projectID', None)
    vendorID=request.POST.get('vendorID',None)
    expenseAmount = request.POST.get('expenseAmount', '0')
    expenseStatus = request.POST.get('expenseStatus','Unknown')
    expenseType = request.POST.get('expenseType', '404')
    expenseDate=request.POST.get('expenseDate','01-02-2000')
    expenseDetails = request.POST.get('expenseDetails','No details found')
    expenseAttachment=request.POST.get('expenseAttachment')
    expenseExtraWorkBoolean=request.POST.get('checkExtraWork',False)
    expensePaid=request.POST.get('expensePaid',True)

    currentExpense = vendorExpense.objects.get(pk=expenseID)
    currentExpense.project=project.objects.get(pk=projectID)
    currentExpense.vendor=vendor.objects.get(pk=vendorID)
    currentExpense.expenseAmount = expenseAmount
    currentExpense.expenseStatus = expenseStatus
    currentExpense.expenseType = expenseType
    currentExpense.expenseDate=expenseDate
    currentExpense.expenseDetails = expenseDetails
    #currentExpense.expenseAttachment=expenseAttachment
    currentExpense.expenseExtraWorkBoolean=expenseExtraWorkBoolean
    currentExpense.expensePaid=expensePaid
    currentExpense.save()

    redirectToinvoices = redirect('/accountManagement/allVendorExpense')
    return redirectToinvoices


@login_required(login_url="/")
def editGeneralExpenseFunction(request):
    from accountManagement.models import generalExpense

    expenseID = request.POST.get('expenseID')
    projectID = request.POST.get('projectID', None)
    expenseReceipient = request.POST.get('expenseReceipient',None)
    expenseAmount = request.POST.get('expenseAmount', '0')
    expenseStatus = request.POST.get('expenseStatus','Unknown')
    expenseType = request.POST.get('expenseType', '404')
    expenseDate= request.POST.get('expenseDate', '01-02-2000')
    expenseDetails = request.POST.get('expenseDetails','No details found')
    expenseAttachment=request.POST.get('expenseAttachment')
    expenseExtraWorkBoolean=request.POST.get('checkExtraWork','False')

    newexpense = generalExpense.objects.get(pk=expenseID)
    newexpense.project=project.objects.get(pk=projectID)
    newexpense.expenseAmount = expenseAmount
    newexpense.expenseReceipient=expenseReceipient
    newexpense.expenseStatus = expenseStatus
    newexpense.expenseType = expenseType
    newexpense.expenseDate=expenseDate
    newexpense.expenseDetails = expenseDetails
    newexpense.expenseAttachments=expenseAttachment
    newexpense.expenseExtraWorkBoolean=expenseExtraWorkBoolean
    newexpense.save()


    redirectToinvoices = redirect('/accountManagement/aMgm')
    return redirectToinvoices




@login_required(login_url="/")
def removeGeneralExpense(request,id):
    from invoiceManagement.models import invoice
    from accountManagement.models import generalExpense

    currentExpense = generalExpense.objects.get(expenseID=id)
    currentInvoice = invoice.objects.get(pk=currentExpense.operatingSourceInvoice_id)
    currentInvoice.invoiceRemainingAmount += int(currentExpense.expenseAmount)

    if currentInvoice.invoiceRemainingAmount > 0:
            currentInvoice.invoiceRemainingStatus = "remaining"

    currentInvoice.save()
    currentExpense.delete()
    redirectSummary = redirect('/accountManagement/aMgm')
    return redirectSummary


@login_required(login_url="/")
def removeProjectExpense(request,id):
    from invoiceManagement.models import invoice

    currentExpense = projectExpense.objects.get(expenseID=id)
    currentInvoice = invoice.objects.get(pk=currentExpense.projectSourceInvoice_id)
    currentInvoice.invoiceRemainingAmount += int(currentExpense.expenseAmount)

    if currentInvoice.invoiceRemainingAmount > 0:
        currentInvoice.invoiceRemainingStatus = "remaining"

    currentInvoice.save()
    currentExpense.delete()
    redirectSummary = redirect('/accountManagement/aMgm')
    return redirectSummary




