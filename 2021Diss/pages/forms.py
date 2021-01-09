from django.forms import ModelForm# ModelForm Import for use of database interaction with Form
from .models import Student#Model Import for use within StudentForm
from django import forms#Forms Import for Form functions within code
from django.core import validators#Import of validation methods for fields within code

class StudentForm(ModelForm):#defining the form for enrolment 
        class Meta:#data type
            model = Student#defining model for use within the form
            fields = [#array of fields to be output to view
                'Username',#for later authentication 
                'Password', #for later authentication 
                'studentForename',#Generic enrolment & user data 
                'studentSurname',#Generic enrolment & user data 
                'studentContactnumber',#Generic enrolment & user data 
                'studentEmail',#Generic enrolment & user data  
                'studentEnglish',#Indication on pocession of English GCSE qualification 
                'studentMaths',#Indication on pocession of Maths GCSE qualification  
                'TotalUCAS',#Indication on UCAS points total when above the 104 point limit  
                'PathwayName',#Identification for later reports
                'LGA1',#Identification for later reports, informed by LGA_Choices01
                'LGA2',#Identification for later reports, informed by LGA_Choices02
                'LGA3',#Identification for later reports, informed by LGA_Choices03 
                'LGA4',#Identification for later reports, informed by LGA_Choices04 
                'LGA5'#Identification for later reports, informed by LGA_Choices05
                ]
        
        def SupCourseEnrol():#Defining the method for changing SupCourse boolean state dependant on LGA_Choices0X used within form and post with rest of information to database

            if self.instance (StudentForm.LGA1) == '3' or input(LGA1) == '4' or input(LGA1) =='5':#declaring if statement for current instance of form to see if the StudentForm has a field value of a certain type
                self.Student.SupCourse01 == True(POST)#change SupCourse01 to True and post to database with rest of information

            if self.instance (LGA2) == '3' or input(LGA2) == '4' or input(LGA2) =='5':#Following the same logic as an LGA1 post
                self.Student.SupCourse02 == True(POST)#Following the same logic as an LGA1 post, change SupCourse02 to True

            if self.instance (LGA3) == '3' or input(LGA3) == '4' or input(LGA3) =='5':#Following the same logic as an LGA1 post
                self.Student.SupCourse03 == True(POST)#Following the same logic as an LGA1 post, change SupCourse03 to True

            if self.instance (LGA4) == '3' or input(LGA4) == '4' or input(LGA4) =='5':#Following the same logic as an LGA1 post
                self.Student.SupCourse04 == True(POST)# Following the same logic as an LGA1 post, change SupCourse04 to True

            if self.instance (LGA5) == '3' or input(LGA5) == '4' or input(LGA5) =='5':#Following the same logic as an LGA1 post
                self.Student.SupCourse05 == True(POST)# Following the same logic as an LGA1 post, change SupCourse05 to True


        def clean(self):#defining the method to be used for data validation for the form fields of StudentForm
            super(StudentForm, self).clean()#Calling super method from django imported functions within StudentForm
            Username = self.cleaned_data.get('Username')#define the username field to use the cleaned_data function and get field data from Username
            Password = self.cleaned_data.get('Password')#define the username field to use the cleaned_data function and get field data from Password
            studentForename = self.cleaned_data.get('studentForename')#define the username field to use the cleaned_data function and get field data from Forename
            studentSurname = self.cleaned_data.get('studentSurname')#define the username field to use the cleaned_data function and get field data from Surname
            studentContactnumber = self.cleaned_data.get('studentContactnumber')#define the username field to use the cleaned_data function and get field data from Contact Number
            studentEmail = self.cleaned_data.get('studentEmail')#define the username field to use the cleaned_data function and get field data from Email Address
            studentEnglish = self.cleaned_data.get('studentEnglish')#define the username field to use the cleaned_data function and get field data for English Grade
            studentMaths = self.cleaned_data.get('studentMaths')#define the username field to use the cleaned_data function and get field data for Maths Grade
            TotalUCAS = self.cleaned_data.get('TotalUCAS')#define the username field to use the cleaned_data function and get field data from TotalUCAS


            if len(Username) < 8:#If the username has less then 8 characters
                self.errors['Username'] = self.error_class(['Minimum of 8 characters required'])#post error message 
            
            if len(Password) < 9:#If the password has less then 9 characters
                self.errors['Password'] = self.error_class(['Minimum of 9 characters required'])#post error message
            

            if len(studentContactnumber) < 11:#add a type that is specific for integers
                self.errors['studentContactnumber'] = self.error_class(['11 characters required'])#post error message
            if len(studentContactnumber) > 11:#If the contact number field has less than 11 characters in
                self.errors['studentContactnumber'] = self.error_class(['11 characters required'])#post error message
            
            if int(TotalUCAS) < 104:#If the inputted UCAS points is less than 104
                self.errors['TotalUCAS'] = self.error_class(['Minimum of 104 points required'])#post error message

            return self.cleaned_data#continue to POST

            
        