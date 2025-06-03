from django.urls import path
from . import views

urlpatterns=[
    path('employee_index/',views.employee_index,name='employee_index'),
    path('employee_details/',views.employee_details,name="employee_details"),
    path('employee_appmade/', views.employee_appmade, name='employee_appmade'),
    path('employee_appform/', views.employee_appform, name='employee_appform'),
    path('employee_appreceived/', views.employee_appreceived, name='employee_appreceived'),
    path('employee_makegrievance/', views.employee_makegrievance, name='employee_makegrievance'),
    path('employee_viewgrievance/', views.employee_viewgrievance, name='employee_viewgrievance'),
    path('employee_griform/', views.employee_griform, name='employee_griform'),
    path('employee_doctor/', views.employee_doctor, name='employee_doctor'),
]
