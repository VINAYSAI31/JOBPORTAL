from django.shortcuts import render
from .models import *



# Create your views here.
def viewjobs(request):
      return render(request,'jobseeker/viewjobs.html')

