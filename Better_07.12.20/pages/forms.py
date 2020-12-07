from django.forms import ModelForm
from .models import Student
from .models import StudentNE

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName']


class StudentFormNE(ModelForm):
    class Meta:
        model = StudentNE
        fields = ['studentID', 'studentForename', 'studentSurname', 'studentContactnumber', 'studentEmail', 'studentEnglishPassed', 'studentMathsPassed', 'studentUCASvalue', 'PathwayName']
        
    
    
