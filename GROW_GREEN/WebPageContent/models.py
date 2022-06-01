from django.db import models

# Create your models here.

class HomeContent(models.Model):
    """
        class for managing home page content
        
        slider_title : title of slider images
        slider_title_descripiton : detailded desrciption of title
        slider_images : images of slider
        tree_plantation_map_title : title of tree plantation map
        tree_plantation_map_image : image or map for tree plantation 
        
    """
    slider_title = models.CharField(max_length=100)
    slider_title_descripiton = models.CharField(max_length=400)
    slider_images = models.ImageField(upload_to='media/sliderImages/ %Y/ %m/ %d/')
    tree_plantation_map_title = models.CharField(max_length=100)
    tree_plantation_map_image = models.ImageField(upload_to='media/sliderImages/ %Y/ %m/ %d/')

    
    def __str__(self):
        return self.slider_title_descripiton


class HomePageTrees(models.Model):
    tree_name = models.CharField(max_length=50)
    tree_details = models.CharField(max_length=200)
    tree_image = models.ImageField(upload_to='media/treePlantedImages/ %Y/ %m/ %d/')


    def __str__(self):
        return self.tree_details