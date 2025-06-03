from django.shortcuts import render
from .models import *
from appraisalapp.models import Employee
from employeeapp.models import Appraisal, Grievance

# Create your views here.
def admin_index(request):
    return render(request,"admin_index.html")

def admin_register(request):
    emp= Employee.objects.all()
    return render(request,"admin_register.html", { 'empdetails':emp }) 

def admin_appraisal(request):
    app= Appraisal.objects.all()
    return render(request, "admin_appraisal.html", { 'appdetails': app})

def admin_grievance(request):
    gri= Grievance.objects.all()
    return render(request, "admin_grievance.html", { 'grievance': gri})

def admin_doctor(request):
    return render(request, "admin_doctor.html")
