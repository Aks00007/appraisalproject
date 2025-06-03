from django.urls import path
from . import views

urlpatterns=[
    path('admin_index/',views.admin_index,name='admin_index'),
    path('admin_register/',views.admin_register,name='admin_register'),
    path('admin_appraisal/', views.admin_appraisal, name='admin_appraisal'),
    path('admin_grievance/', views.admin_grievance, name='admin_grievance'),
    path('admin_doctor/', views.admin_doctor, name='admin_doctor'),
]
