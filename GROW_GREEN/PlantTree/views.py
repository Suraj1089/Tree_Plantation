from django.shortcuts import render

# Create your views here.

#function for testing wbsite UI
def home(request):
    return render(request, 'base.html')
    # pass
    
def navbar(request):
    return render(request,'includes/navbar.html')
   
    
def footer(request):
    return render(request,'includes/footer.html')


def test(request):
    return render(request, 'PlantTree/index.html')

def plant_ui(request):
    return render(request, 'PlantTree/plant.html')