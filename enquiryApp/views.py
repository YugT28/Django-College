from django.shortcuts import render
from django.http import HttpResponse
from .models import Enquiry
from .forms import EnquiryForm

from django.db.models import F
from .forms import EnquiryForm,Options

# Create your views here.
def fillEnquiry(request):
    x=Enquiry
    if request.method == 'POST':
        x=Enquiry()
        x.Email_ID=request.POST['Email_ID']
        x.Question=request.POST['Question']
        x.save()
    #     print(request.POST)
    #------------------------------------
    # if request.method == 'POST':
    #     Enquiry.objects.create(Email_ID=request.POST['Email_ID'],Question=request.POST['Question'])
    return render(request,"enquiryApp/fillenquiry.html",context={'x':x})

def showEnquiry(request):
    # data=Enquiry.objects.all().values()
    # data=list(data)

    #-------------------------------------------------------


    # data=Enquiry.objects.raw("SELECT * FROM college.enquiryapp_enquiry")
    # data=Enquiry.objects.raw("SELECT * FROM college.enquiryapp_enquiry Join college.enquiryapp_stroke")
    # x=list(data)
    # for i in data:
    #     print(str(i))
    # for i in x:
    #     print(i)
    # print(list(data))
    #--------------------------------------------------------
    # for i in data:
    #     print(i.count)
    # data=Enquiry.objects.all().order_by('-id').values()
    # data = Enquiry.objects.all().order_by('-Question').values()
    # Enquiry.objects.filter(Email_ID=F('collection__id'))
    # data=Enquiry.objects.filter(Email_ID=F('Question'))
    # data = Enquiry.objects.values('Email_ID', 'Question')
    # data=Enquiry.objects.select_related("Trauma").all().values()

    # e=Enquiry.objects.get(pk=1)
    # e.Email_ID='sdfgdfsg'
    # e.save()
    # print(list(data.iterator()))
    # print(data)
    # data=EnquiryForm()
    # sent=False
    # if request.method=='POST':
    #     formss = EnquiryForm(request.POST)
    #     if formss.is_valid():
    #         print(formss.cleaned_data)
    #         sent=False
    #         formss.save(commit=True)

    # data=Parent.objects.select_related('Child').all()
    # data=Child.objects.all().values()
    # data = Child.objects.select_related('Parent').values()
    # data = Child.objects.raw("select * from enquiryapp_parent join enquiryapp_child;")

    # for i in data:
    #     print(i.)
    # data=Options()
    # if request.method=='POST':
    #     p=Options(request.POST)
    #     if p.is_valid():
    #         print(p.cleaned_data)
    #         data=p.cleaned_data
    #
    data=Enquiry.objects.all()
    print(data)
    return render(request,"enquiryApp/showEnquiry.html",context={"data":data})   #,'sent':sent

def homepage(request):
    return render(request,"homepage/homepage.html")