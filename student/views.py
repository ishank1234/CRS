from django.shortcuts import render
from company.forms import LoginForm
from company.models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    print("===================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    log=LoginForm(request.POST or None)
    if log.is_valid():
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/stuLog/stuReg/student_panel')
        else:
            msg='Invalid Credentials'
            log=LoginForm()
            return render(request,'student/log.html',{'err':msg,'form':log})
    return render(request,'student/log.html',{'form':log})
def stuReg(request):
    reg=RegStudent(request.POST or None)
    print(reg.is_valid())
    if reg.is_valid():
        yoc=request.POST.get('Year_Of_Completion')
        roll=request.POST.get('Roll_number')
        name=request.POST.get('Name')
        branch=request.POST.get('branch')
        sex=request.POST.get('sex')
        email=request.POST.get('email')
        dob=request.POST.get('Date_Of_Birth')
        contact=request.POST.get('contact')
        percentile=request.POST.get('percentile')
        hsy=request.POST.get('high_school_year')
        hsp=request.POST.get('high_school_percentage')
        iy=request.POST.get('intermediate_year')
        ip=request.POST.get('intermediate_percentile')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        op = Dept.objects.get(name=branch)
        user=User.objects.create_user(username=roll,password=password)
        f = Stu(d=op, Year_Of_Completion=yoc, Roll_number=roll, Name=name, Sex=sex, DOB=dob, Email=email,
                    Contact=contact, Percentile=percentile, HighSchool=hsy, HighPer=hsp, Intermediate=iy, InterPer=ip,user=user)
        f.save()
        user=authenticate(request,username=roll,password=password)
        if user is not None:
            login(request,user)
            return redirect('stuReg/student_panel')
        else:
            msg='Invalid Credentials'
            log=LoginForm()
            return HttpResponseRedirect('stuLog/stuReg',{'err':msg,'form':reg})
    return render(request,'student/reg.html',{'form':reg})
def student_panel(request):
    b1=Company.objects.exclude(c_name="tpo@knit")
    return render(request,'student/student_panel.html',{'i':b1})
def ajax(request,company_id):
    a1=Company.objects.get(id=company_id)
    a2=Company.objects.exclude(c_name="tpo@knit")
    if Drive.objects.filter(app=a1,stu_Roll=request.user.stu.Roll_number):
        msg="Your data already has been taken!!!"
    else:
        c=Drive(app=a1,stu_Roll=request.user.stu.Roll_number)
        c.save()
        msg="You have applied for the drive!!!!!"
    return render(request,'student/student_panel.html',{'i':a2,'j':a1,'msg':msg})
