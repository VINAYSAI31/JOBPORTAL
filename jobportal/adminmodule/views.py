from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
                messages.info(request, 'Account created successfully!! ')
                user.save()

                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('jobseekerhomepage')
                messages.success(request, 'Logged in successfully as job seeker!')
            elif len(username) == 4:
                return redirect('employeerhomepage')
                messages.success(request, 'Logged in successfully as employer!')
                messages.success(request, 'Logged in successfully as employer!')
            else:
                messages.success(request, 'Logged in successfully!')
                return redirect('projecthomepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'projecthomepage.html')

