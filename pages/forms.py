from django.forms import ModelForm
from.models import Student
from.models import Course
from.models import Pathway

class StudentForm(ModelForm):
    class Meta:
        models = Student, Course, Pathway
        fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'CourseName', 'PathwayName']


#class NEenrollForm(ModelForm):
    #class Meta:
        #model = Student
        #fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName', 'CourseName']
        
    
    
