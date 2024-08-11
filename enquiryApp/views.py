from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testStatic(request):
    return render(request,"enquiryApp/enquiry.html")

def homepage(request):
    return render(request,"homepage/homepage.html")