from django.shortcuts import render, redirect
from .models import *
from appraisalapp.models import Employee, Login

# Create your views here.
def employee_index(request):
    return render(request,"employee_index.html")

def employee_details(request):
    userid=request.session.get('userid')
    emp=Employee.objects.get(userid=userid)
    return render(request,"employee_details.html", { 'e':emp })

def employee_appmade(request):
    userid=request.session.get('userid')
    obj=Appraisal.objects.filter(appraiseruserid=userid)
    return render(request, "employee_appmade.html",{'appdetails':obj})

def employee_appform(request):
    if request.method=="POST":
        appraiseeuserid=request.POST.get('appraiseeuserid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        designation=request.POST.get('designation')
        performancerating=request.POST.get('performancerating')
        appraiseruserid=request.POST.get('appraiseruserid')
        comments=request.POST.get('comments')
        appraisal=Appraisal(appraiseruserid=appraiseruserid, appraiseeuserid=appraiseeuserid, name=name, department=department, designation=designation, performancerating=performancerating, comments=comments)
        appraisal.save()
        return redirect('employeeapp:employee_appmade')
    appraiseruserid=request.session.get('userid')
    name=Employee.objects.get(userid=appraiseruserid)
    return render(request, "employee_appform.html",{'appraiseruserid':appraiseruserid})

def employee_appreceived(request):
    userid=request.session.get('userid')
    obj=Appraisal.objects.filter(appraiseeuserid=userid)
    return render(request, "employee_appreceived.html",{'appdetails':obj})

def employee_makegrievance(request):
    userid=request.session.get('userid')
    obj=Grievance.objects.filter(appraiseruserid=userid)
    return render(request, "employee_griform.html")

def employee_griform(request):
    if request.method=="POST":
        appraiseeuserid=request.POST.get('appraiseeuserid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        designation=request.POST.get('designation')
        appraiseruserid=request.POST.get('appraiseruserid')
        grievance=request.POST.get('grievance')
        grievance=Grievance(appraiseruserid=appraiseruserid, appraiseeuserid=appraiseeuserid, name=name, department=department, designation=designation, grievance=grievance)
        grievance.save()
        return redirect('employeeapp:employee_grievance')
    appraiseruserid=request.session.get('userid')
    name=Grievance.objects.filter(appraiseruserid=appraiseruserid)
    return render(request, "employee_griform.html",{'appdetails':name})

def employee_viewgrievance(request):
    userid=request.session.get('userid')
    obj=Grievance.objects.filter(appraiseruserid=userid)
    return render(request, "employee_viewgrievance.html",{'appdetails':obj})

def employee_doctor(request):
    return render(request, "employee_doctor.html")
