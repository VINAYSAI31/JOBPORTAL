from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def employeerhomepage(request):
    return render(request, 'employeerhomepage.html')

def jobseekerhomepage(request):
    return render(request, 'jobseekerhomepage.html')

def signup(request):
    return render(request, 'signup.html')

def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!! ')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')



