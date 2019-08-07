from django import forms
from django.contrib.auth import get_user_model
from .models import Stu
from django.http import JsonResponse

class RegStudent(forms.Form):
    CHOICES=((1,1),(2,2),(3,3),(4,4))
    branchchoices=(('MCA','MCA'),('IT','IT'),('CS','CS'),('ME','ME'),('EL','EL'),('EE','EE'),('CE','CE'))
    sexchoices=(('male','male'),('female','female'))
    Year_Of_Completion=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Year Of Completion'}))
    Roll_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Roll Number and this is also your userid'}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}))
    branch=forms.ChoiceField(choices=branchchoices)
    sex=forms.ChoiceField(choices=sexchoices)
    Date_Of_Birth=forms.CharField(label="YYYY-MM-DD" )
    contact=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Info'}))
    percentile=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Current Percentile'}))
    high_school_year=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your High School Year'}))
    high_school_percentage=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your HighSchool Percentile'}))
    intermediate_year=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Intermediate year'}))
    intermediate_percentile=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Intermediate Percentile'}))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password:- '}))
    confirm_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password:- '}))

    def clean(self):
        data=self.cleaned_data
        n=self.cleaned_data.get('Name')
        email=self.cleaned_data.get('email')
        contact=self.cleaned_data.get('contact')

        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        Year_Of_Completion=self.cleaned_data.get('Year_Of_Completion')
        high_school_year=self.cleaned_data.get('high_school_year')
        high_school_percentage=self.cleaned_data.get('high_school_percentage')
        intermediate_year=self.cleaned_data.get('intermediate_year')
        intermediate_percentile=self.cleaned_data.get('intermediate_percentile')
        print("===========================???????????????????")
        if password != confirm_password:
            raise forms.ValidationError('password must be matched!!!')
        elif len(password) <6:
            raise forms.ValidationError('Password should be of minimum 6 characters')
        elif '@' not in email:
            raise forms.ValidationError("Enter correct Email")
        elif contact <1000000000 or contact>10000000000:
            raise forms.ValidationError("Invalid contact info.")
        elif (Year_Of_Completion <2018) or (Year_Of_Completion >2025):
            raise forms.ValidationError('Year of completion is incorrect')
        elif (high_school_year <2005) or (high_school_year >2015):
            raise forms.ValidationError('High School Year is Wrong!!!')
        elif high_school_percentage >100:
            print("999999999999999999999999999999999999999999999999")
            raise forms.ValidationError('High school percentage is wrong!!!')
        elif (intermediate_year <2007) or (intermediate_year>2018):
            raise forms.ValidationError('Intermediate Year is wrong!!!')
            if intermediate_year-high_school_year < 2 :
                raise forms.ValidationError('High school Year and Intermediate passing year collapsed!!!')
        elif intermediate_percentile >100:
            raise forms.ValidationError('Intermediate percentage is wrong!!!')

        else:
            return data


    def clean_Roll_number(self):
        Roll_number=self.cleaned_data.get('Roll_number')
        print("---------------",Roll_number)
        q=Stu.objects.filter(Roll_number=Roll_number)
        print("--------------''''''''''''' ",q.exists(),'  ',q)
        if q.exists():
            raise forms.ValidationError('Roll number is already register')
        else:
            print("-----------------<<<<<<<<<<<<<<<<<<<<<")
            return Roll_number

    def clean_Date_Of_Birth(self):
        Date_Of_Birth=self.cleaned_data.get('Date_Of_Birth')
        count=0
        print(type(Date_Of_Birth))
        print("===========>>>>>>>>>>>>>>>>>>>>>")
        if '-' in Date_Of_Birth and len(Date_Of_Birth)==10:
            a=Date_Of_Birth[:4]
            a=int(a)
            if a>=1980 and a<=2005:
                b=Date_Of_Birth[5:7]
                b=int(b)
                if b>0 and b<13:
                    c=Date_Of_Birth[8:10]
                    c=int(c)
                    if c>0 and c<=31:
                        return Date_Of_Birth
            raise forms.ValidationError("Date Of Birth is wrong")
        else:
            print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
            raise forms.ValidationError("DOB format should be : YYYY-MM-DD")
