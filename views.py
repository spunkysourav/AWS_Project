from django.shortcuts import render
from django.http.response import HttpResponse
from.cusbll import Customer
def cmsview (request):
    if request.method=="POST":
        Cus_Id = request.POST.get ('Cus_Id', 'NA')
        Name = request.POST.get ('Name', 'NA')
        Address = request.POST.get ('Address', 'NA')
        Mobile_No = request.POST.get ('Mobile_No', 'NA')
        cus=Customer()
        cus.id=Cus_Id
        cus.name=Name
        cus.address=Address
        cus.mobileno=Mobile_No
        cus.addCustomer()
        return HttpResponse ("Customer Added Successfully!!")
    else:
        return render(request, 'cmsform.html')