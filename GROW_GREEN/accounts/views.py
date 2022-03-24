from django.shortcuts import render

# Create your views here.
def register(request):  #function for signup user
    return render(request,'includes/login-signup-modal.html')


def login(request):   #function for sign in user
    pass