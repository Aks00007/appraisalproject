from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Employee,Login

# Create your views here.
def index(request):
    #nw=News.objects.all()
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        department=request.POST.get('department')
        designation=request.POST.get('designation')
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        employee=Employee(userid=userid, name=name, gender=gender, fname=fname, mname=mname, emailaddress=email, contactno=contact, dob=dob, address=address, department=department, designation=designation, password=password)
        employee.save()
        return redirect('appraisalapp:index')
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        usertype=request.POST.get('usertype')
        try:
            user=Login.objects.get(userid=userid, password=password, usertype=usertype)
            if(usertype=='Admin'):
                request.session['userid']=user.userid
                return redirect(reverse('adminapp:admin_index'))
            elif (usertype=='Employee'):
                request.session['userid']=user.userid
                return redirect(reverse('employeeapp:employee_index'))
            else:
                return redirect(reverse('appraisalapp:login'))
        except Login.DoesNotExist:
            messages.error(request, "INCORRECT USERNAME OR PASSWORD")
            return render(request, "login.html", {'error': "INCORRECT USERNAME OR PASSWORD"})
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
