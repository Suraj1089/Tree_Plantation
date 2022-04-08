from django.shortcuts import render

# Create your views here.
def register(request):  #function for signup user
    return render(request,'accounts/register.html')


def login(request):   #function for sign in user
    return render(request, 'accounts/login.html')

def logout_user(request):   #function for sign in user
    return render(request, 'accounts/login.html')


def dashboard(request):   #function for sign in user
    return render(request, 'accounts/dashboard.html')