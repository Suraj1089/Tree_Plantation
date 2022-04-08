from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
def register(request):
    #function for signup user
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exists')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('register')
        
                else:   
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"account crated succesfully")
                    return redirect('login')
        else:
            messages.error(request, 'password do not match with confirm password')
            return redirect('register')
        
    return render(request,'accounts/register.html')


def login(request):   #function for sign in user
    return render(request, 'accounts/login.html')


def logout_user(request):   #function for sign in user
    logout(request)
    return redirect('accounts/register.html')


def dashboard(request):   #function for sign in user
    return render(request, 'accounts/dashboard.html')

def about(request):   #function for sign in user
    return render(request, 'accounts/about.html')