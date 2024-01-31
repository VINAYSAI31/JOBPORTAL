from django.shortcuts import render

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')
def employeerhomepage(request):
    return render(request,'employeerhomepage.html')
def jobseekerhomepage(request):
    return render(request,'jobseekerhomepage.html')

