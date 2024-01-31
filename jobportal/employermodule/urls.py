from django.contrib import admin
from django.urls import path, include
from . import   views

urlpatterns = [
     path('jobpost',views.jobpost,name='jobpost'),
     path('add_job_details',views.add_job_details,name='add_job_details'),
     path('viewjob',views.view_job_details,name='view_job_details'),
]