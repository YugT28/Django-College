from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    Student_Roll=forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Add your custom CSS class here
            'placeholder': 'Enter a number'  # You can also add other attributes
        }))
    Marks = forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Add your custom CSS class here
            'placeholder': 'Enter a number'  # You can also add other attributes
        }))
    class Meta:
        model=Result
        fields=['Cid']
        widgets={
            'Cid': forms.Select(attrs={'class': 'form-select'})
        }




class Branch_Choise(forms.Form):
    MEMBERSHIP_CHOICES=[(3,'Civil'),(2,'Mechanical'),(1,'Computer'),(0,'ALL')]
    branch_choise = forms.ChoiceField(choices=MEMBERSHIP_CHOICES,widget=forms.Select(attrs={'class':"form-select",'aria-label':"Default select example"}))

class Course_Choise(forms.Form):
    MEMBERSHIP_CHOICES = [
    (12	,'Structural Analysis'),
    (11,	'Enviornmental'),
    (10	,'Geotechnology'),
    (9	,'Construction Management'),
    (8	,'Engineering Drawing'),
    (7	,'Thermodynamics'),
    (6	,'Control System'),
    (5	,'Fluid Mechanics'),
    (4,	'NLP'),
    (3	,'Discreate Mathematics'),
    (2	,'Conputer Vision'),
    (1	,'Machine Learning'),(0,'ALL')]
    course_choise = forms.ChoiceField(choices=MEMBERSHIP_CHOICES,widget=forms.Select(attrs={'class':"form-select",'aria-label':"Default select example"}))



class Student_Roll(forms.Form):
    student_roll = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Add your custom CSS class here
            'placeholder': 'Enter a number'  # You can also add other attributes
        }))