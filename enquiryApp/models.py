from django.db import models

# Create your models here.
class Enquiry(models.Model):
    Email_ID=models.EmailField()
    Question=models.TextField()

