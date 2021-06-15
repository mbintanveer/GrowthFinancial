from datetime import datetime

from django.contrib.auth.decorators import login_required


from django.db.models import Sum
from django.shortcuts import render, redirect
from accountManagement.models import generalExpense
from vendorManagement.models import vendor
from accountManagement.decorators import top_level_required


@login_required(login_url='/')
def vLanding(request):
    return render(request, 'vLanding.html')

@login_required(login_url='/')
def vMgm(request):
    vendorObjects= vendor.objects.all()
    vendorOngoing=[]

    for currentVendor in vendorObjects:
        if (currentVendor.getAmount() !=0):
            vendorOngoing.append(currentVendor)

    parameters = {'vendorOngoing': vendorOngoing}
    return render(request, 'vMgm.html',parameters)

@login_required(login_url='/')
def vSpecific(request,id):
    currentVendor = vendor.objects.get(pk=id)
    parameters = {'currentVendor': currentVendor}
    return render(request,'vSpecific.html',parameters)


@login_required(login_url='/')
def vAdd(request):
    from accountManagement.models import project

    projectList = project.objects.all()
    vendorTypeList = {
        "Labour"
    }

    parameters = {'projectList': projectList, 'vendorTypeList':vendorTypeList}
    return render(request,'vAdd.html',parameters)



@login_required(login_url='/')
def vEdit(request, id):
    currentVendor = vendor.objects.get(pk=id)
    parameters = {'currentVendor': currentVendor}
    return render(request, 'vEdit.html', parameters)


@login_required(login_url='/')
@top_level_required(allowed_roles=['top_level'])
def vSummary(request):
    from projectManagement.models import project,owner

    projectList = project.objects.all()
    ownerList=owner.objects.all()
    vendorList = vendor.objects.all()
    vendorListCompleted = vendor.objects.all()
    vendorListOngoing=vendor.objects.all()

    vendorCompletedSum =vendorListCompleted.aggregate(Sum('vendorAmount'))['vendorAmount__sum']
    vendorOngoingSum= vendorListOngoing.aggregate(Sum('vendorAmount'))['vendorAmount__sum']

    #NONE TYPE CHECK
    if vendorCompletedSum==None:
        vendorCompletedSum =0

    if vendorOngoingSum==None:
        vendorOngoingSum=0

    vendorCompletedSum/=1000000
    vendorOngoingSum/=1000000

    parameters = {'vendorList': vendorList , 'projectList':projectList,'ownerList':ownerList,
                  'vendorCompletedSum':vendorCompletedSum,'vendorOngoingSum':vendorOngoingSum}

    return render(request,'vSummary.html',parameters)


@login_required(login_url='/')
def vCompleted(request):

    vendorObjects = vendor.objects.all()
    vendorsCompleted = []

    for currentVendor in vendorObjects:
        if (currentVendor.getAmount() == 0):
            vendorsCompleted.append(currentVendor)


    parameters = {'vendorsCompleted': vendorsCompleted}
    return render(request, 'vCompleted.html', parameters)



@login_required(login_url='/')
def addVendorFunction(request):
    vendorName = request.POST.get('vendorName')
    vendorOwner = request.POST.get('vendorOwner')
    vendorCategory=request.POST.get('vendorCategory')


    newVendor = vendor.objects.create(vendorName=vendorName,vendorOwner=vendorOwner,
                                      vendorCategory=vendorCategory,vendorAmount=0)
    newVendor.save()

   # params={'display':'Your project named: %s - Owner: %s has been created'%(vendorName,vendorOwner)}

    vMgm = redirect(('/vendorManagement/vMgm'))
    return vMgm


@login_required(login_url='/')
def editVendorFunction(request):

    from vendorManagement.models import vendor
    vendorID = request.POST.get('vendorID')
    vendorName=request.POST.get('vendorName')
    vendorOwner=request.POST.get('vendorOwner')
    vendorCategory=request.POST.get('vendorCategory')

    currentVendor = vendor.objects.get(pk=vendorID)
    currentVendor.vendorName = vendorName
    currentVendor.vendorName = vendorName
    currentVendor.vendorOwner= vendorOwner
    currentVendor.vendorCategory = vendorCategory
    currentVendor.save()

    redirectTovendors = redirect('/vendorManagement/vMgm')
    return redirectTovendors
