from django.forms import ModelForm
from .models import Student
from .models import Pathway
from .models import Course
#from .models import StudentNE

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentUsername', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName', 'LGA1', 'LGA2', 'LGA3', 'LGA4', 'LGA5' ]

class LGAForm(ModelForm):
    class Meta:
        models = Student, Pathway, Course
        fields = ['studentUsername', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName']

#class StudentFormNE(ModelForm):
    #class Meta:
        #model = StudentNE
        #fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName']
        
    
    
