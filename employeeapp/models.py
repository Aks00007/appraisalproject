from django.db import models

# Create your models here.
class Appraisal(models.Model):
    appraiseruserid=models.CharField(max_length=100, default=0)
    appraiseeuserid=models.CharField(max_length=100, default=0)
    name=models.CharField(max_length=256, null=False, blank=False)
    department=models.CharField(max_length=128)
    designation=models.CharField(max_length=128)
    performancerating=models.IntegerField(max_length=5)
    comments=models.TextField(max_length=2000)

class Grievance(models.Model):
    appraiseruserid=models.CharField(max_length=100, default=0)
    appraiseeuserid=models.CharField(max_length=100, default=0)
    name=models.CharField(max_length=256, null=False, blank=False)
    department=models.CharField(max_length=128,default='admin')
    designation=models.CharField(max_length=128,default='clerk')
    grievance=models.TextField()