from django.contrib import admin
from django.urls import path, include
from .import  views

urlpatterns = [
path('viewjobs',views.viewjobs,name='viewjobs'),
]