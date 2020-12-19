from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'Username', 
            'Password', 
            'studentForename', 
            'studentSurname', 
            'studentContactnumber', 
            'studentEmail', 
            'studentEnglish', 
            'studentMaths', 
            'TotalUCAS', 
            'PathwayName', 
            'LGA1', 
            'LGA2', 
            'LGA3', 
            'LGA4', 
            'LGA5'
            ]

