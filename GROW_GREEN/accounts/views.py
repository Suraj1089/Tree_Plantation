from ast import Not
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


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