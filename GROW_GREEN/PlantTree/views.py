from django.shortcuts import render

# Create your views here.

#function for testing wbsite UI
def say_hello(request):
    return render(request, 'base.html')
    # pass