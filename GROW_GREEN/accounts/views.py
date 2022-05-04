
from curses import use_env
from multiprocessing import context
from django.forms import EmailInput
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import ContactGrowGreen
from .forms import ContactGrowGreenForm


def register(request):
    #function for signup user
    """
        function for registering user
        firstname : first name of user
        lastname : last name of user 
        username : user name of user
        email : email of user
        password : password
        return : HttpRespose
    """
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        #checking password and confirm password are same or not
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


def login(request):
    #function for sign in user
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user) 
            messages.success(request,"login succesfully")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid credentials")
            
    return render(request, 'accounts/login.html')


def logout_user(request):
    """
        function for logout user
    """
    logout(request)
    return redirect('register')


@login_required(login_url='login')
def dashboard(request): 
    """
        function for displaying user account
        login_required = decorator used to restrict anyone from accessing dashboard without login
    """
    return render(request, 'accounts/dashboard.html')



def about(request):   #function for sign in user
    return render(request, 'accounts/about.html')



def contact(request):
    return render(request, 'accounts/contact.html')



def contact_growgreen(request):
    # return render(request,'accounts/contact.html')
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_email = request.POST['user_email']
        user_state = request.POST['State']
        user_message = request.POST['usermessage']
        
        contact_user = ContactGrowGreen(first_name=first_name,last_name=last_name,user_email=user_email,user_state=user_state,user_message=user_message)
        contact_user.save()
        
        messages.success(request,"thank you for contacting us our representative get touch with you soon!!")
        return redirect('home')

    else:
        return render(request,'accounts/contact.html')
        
    