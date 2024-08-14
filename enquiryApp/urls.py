from django.urls import path
from .views import fillEnquiry,showEnquiry






urlpatterns = [
    path("",fillEnquiry, name="fillEnquiry"),
    path("showEnquiry/", showEnquiry, name='showEnquiry')
]

