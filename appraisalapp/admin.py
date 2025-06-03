from django.contrib import admin
from . models import Employee, Admin, Login

# Register your models here.
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Login)
