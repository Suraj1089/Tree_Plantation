
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from GROW_GREEN import settings
from .models import PlantaTree

# Create your views here.

# function for testing wbsite UI


def home(request):
    return render(request, 'index.html')
    # pass


def navbar(request):
    return render(request, 'includes/navbar.html')


def footer(request):
    return render(request, 'includes/footer.html')


def test(request):
    return render(request, 'PlantTree/index.html')


def plant_ui(request):
    return render(request, 'PlantTree/plant.html')


def plant_tree(request):

    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        tree_name = request.POST['treename']
        date = request.POST['date']
        # tree_pictures = request.POST['Image']
        tree_pictures = request.FILES.get('Image')
        tree_description = request.POST['date']

        # points = settings.

        plat_tree = PlantaTree(first_name=first_name, last_name=last_name, username=user_name,
                               tree_name=tree_name, tree_pictures=tree_pictures, tree_description=tree_description)

        plat_tree.save()

        return redirect('home')

    else:
        return render(request, 'PlantTree/plant.html')
