from django import forms
from django.core import validators
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    # def star(value):
    #     # raise forms.ValidationError("It is Not OK")
    #     print("Thats Not how we do")

    class Meta:
        model=Enquiry
        # exclude=['Question']

        fields='__all__'

class Options(forms.Form):
    MEMBERSHIP_CHOICES=[('G','GOLD'),('S','Silver'),('B','Bronze')]
    # OPTION_CHOICES = [
    #     ('1', 'Option 1'),
    #     ('2', 'Option 2'),
    #     ('3', 'Option 3'),
    #     ('4', 'Option 4'),
    # ]
    option_field = forms.ChoiceField(choices=MEMBERSHIP_CHOICES)

    # membership = forms.CharField(max_length=1, choice=MEMBERSHIP_CHOICES, default='B')

    # int=forms.IntegerField()
    # date=forms.DateField()
    # time=forms.TimeField()
    # location=forms.CharField(widget=forms.Textarea,validators=[star])




   # def clean_location(self):
    #     inp=self.cleaned_data['location']
    #     if inp=='Pune':
    #         print("FUCK")
    #         print(self.cleaned_data['location'])
    #     return inp   #will retrun to cleaner_data
    #
