from django.shortcuts import render

# Create your views here.

def say_hello(request):
    return render(request, 'base.html')
    # pass