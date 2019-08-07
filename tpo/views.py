from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from company.models import *
from company.forms import LoginForm
from django.http import HttpResponseRedirect
from student.models import *
# Create your views here.
def logtpo(request):
    log=LoginForm(request.POST or None)
    if log.is_valid():
        username=request.POST.get('username')
        password=request.POST.get('password')
        msg='Invalid Credentials'
        if username=="tpo@knit1234" and password=="tpo@knit":

            user=authenticate(request,username=username,password=password)
            print("In login---------------------------------->>>>>>>>>>>>>>>>>>>>")
            if user is not None:
                login(request,user)
                c=Company.objects.all()
                return redirect('/tpo')
            else:
                msg='Invalid Credentials'
                log=LoginForm()
                return render(request,'tpo/c1.html',{'err':msg,'form':log})
        else:
            return render(request,'tpo/c1.html',{'err':msg,'form':log})
    return render(request,'tpo/c1.html',{'form':log})

def ishank(request):
    logout(request)
    return HttpResponseRedirect('/company')


def tpo(request):
    c=Company.objects.all()
    return render(request,'tpo/tpo.html',{'c':c})
def placed(request,company_id):
    b=Company.objects.get(id=company_id)
    c=b.select_set.all()
    return render(request,'tpo/place.html',{'c':c})
def dlt(request,company_id):
    b=Company.objects.get(id=company_id).delete()
    c=Company.objects.exclude(c_name="tpo@knit")
    return render(request,'tpo/tpo.html',{'c':c})
