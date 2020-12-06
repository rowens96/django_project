from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue']


#class NEenrollForm(ModelForm):
    #class Meta:
        #model = Student
        #fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName', 'CourseName']
        
    
    
