from django.db import models

# Create your models here.
class Employee(models.Model):
    userid = models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    dob=models.CharField(max_length=30)
    address=models.TextField()
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    contactno=models.CharField(max_length=10)
    emailaddress=models.EmailField(max_length=254)
    password=models.CharField(max_length=30)

class Admin(models.Model):
    userid=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.EmailField(max_length=254)

class Login(models.Model):
    userid = models.CharField(default='aks007', max_length=100, primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=20)
