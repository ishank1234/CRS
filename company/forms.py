from django import forms
from django.contrib.auth import get_user_model
from .models import *
from django.core.exceptions import ValidationError
from django.http import JsonResponse

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
class RegForm(forms.Form):
    company_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}))
    hr_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'HR Name'}))
    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    contact_info=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Info'}))
    drive_venue=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Placement Drive Venue'}))
    drive_date= forms.DateField()
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'please remember your user id always.'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password:- '}))
    confirm_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password:- '}))
    def clean(self):
        data=self.cleaned_data
        email=self.cleaned_data.get("email")
        contact=self.cleaned_data.get("contact_info")
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        print("Helllllllllllllllllllllllllllllooooooooooooooooooooooooooo")
        if password != confirm_password:
            raise forms.ValidationError('password must be matched!!!')
        elif len(password) <6:
            raise forms.ValidationError('Password should be of minimum 6 characters')
        elif '@' not in email:
            raise forms.ValidationError("Enter correct Email")
        elif contact <1000000000 or contact>10000000000:
            raise forms.ValidationError("Invalid contact info.")
        else:
            return data

    def clean_drive_date(self):
        Date_Of_Birth=self.cleaned_data.get('drive_date')
        count=0
        print("ppppppppppppppppppppppppppppppppppppppppppppppppppp")
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
            raise forms.ValidationError("Date Of drive is wrong")
        else:
            print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
            raise forms.ValidationError("Drive date should be in this format : YYYY-MM-DD")
