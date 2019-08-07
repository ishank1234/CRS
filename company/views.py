from django.shortcuts import render
from .forms import *
from student.models import *
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
def company_panel(request):
    return render(request,'company/company_panel.html')

def log(request):
    log=LoginForm(request.POST or None)
    reg=RegForm(request.POST or None)
    if log.is_valid():
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print("In login---------------------------------->>>>>>>>>>>>>>>>>>>>")
        if user is not None:
            login(request,user)
            return redirect('/company/company_panel')
        else:
            msg='Invalid Credentials'
            log=LoginForm()
            reg=RegForm(request.POST or None)
            return render(request,'company/c1.html',{'err':msg,'form':log,'reg':reg})
    return render(request,'company/c1.html',{'form':log,'reg':reg})

def home(request):
    print("home")
    return render(request,'home.html')

def signUp(request):
    if request.method=="POST":
        company_name=request.POST.get('company_name')
        hr_name=request.POST.get('hr_name')
        email=request.POST.get('email')
        contact_info=request.POST.get('contact_info')
        drive_venue=request.POST.get('drive_venue')
        drive_date=request.POST.get('drive_date')

        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        print(username)
        user=User.objects.create_user(username=username,password=password)
        user.save()
        f = Company(c_name=company_name, c_HR_name=hr_name, c_email=email, c_contact=contact_info, c_venue=drive_venue, c_date=drive_date,user=user)
        print("------------------>>>>>>>>>>>>>>>>-----------------------")
        f.save()
        print("In sign Up")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/company/company_panel')
        return HttpResponse("Sorry some problem occured")
def search(request):
    a = request.POST.get('w1')
    a1 = request.POST.get('w2')
    a2 = request.POST.get('w3')
    a3 = request.POST.get('w4')
    a4 = request.POST.get('w5')
    a5 = request.POST.get('w6')
    a6 = request.POST.get('w7')
    lookup=Q(name=a)|Q(name=a1)|Q(name=a2)|Q(name=a3)|Q(name=a4)|Q(name=a5)|Q(name=a6)
    x=Dept.objects.filter(lookup)
    z=request.POST['t3']
    print(x)
    w=[]
    e=Company.objects.get(id=request.user.company.id)
    y=e.drive_set.all()
    print(y)
    p=[]
    for i in y:
        p.append(i.stu_Roll)
        print(i.stu_Roll)
    j=0
    for i in x:
        print(i)
        for o in p:
            print("Inside")
            w.append(i.stu_set.filter(Year_Of_Completion=z,Roll_number=o))
            print(w,"j")

    return render(request,'company/comlist.html',{'rec':w,'e':e})

def ishu(request,stu_Roll_number):
    a=Stu.objects.get(pk=stu_Roll_number)
    p=a.d
    return render(request,'company/ishu.html',{'i':a,'p':p})
def selected(request,stu_Roll_number):
    msg="You have Selected "
    more="Return back to select more talents of our institute"
    c=Company.objects.get(id=request.user.company.id)
    a=Stu.objects.get(pk=stu_Roll_number)
    if Select.objects.filter(com=c,stu_roll=stu_Roll_number):
        msg="You already has been selected this student!!"
    else:
        d=Select(com=c,stu_roll=stu_Roll_number)
        d.save()

    return render(request,'company/ishu.html',{'i':a,'msg':msg,'more':more})
def hired(request,company_id):
    e=Company.objects.get(id=company_id)
    y=e.select_set.all()
    p=[]
    for i in y:
        p.append(i.stu_roll)
        print(i.stu_roll)
    a=[]
    for l in p:
        a.append(Stu.objects.filter(Roll_number=l))
    print(a)
    return render(request,'hired.html',{'a':a})
