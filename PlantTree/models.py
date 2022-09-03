
from django.db import models
from django.contrib.auth.models import AbstractUser
import binascii
from uuid import uuid4
import os 
import random


def generate_key(num):
        return binascii.hexlify(os.urandom(20)).decode()

class PlantaTree(models.Model):

    tree_choices = [
            ('N', 'Neem'),
            ('K','Karanja'),
            ('M','Mango'),
            ('J','Jamun'),
            ('B','Banyan'),
            ('A','Amrood'),
            ('BB','Bamboo'),
            ('BE','Ber'),
            ('NI','Banyan'),
            
        ]
    tree_planted_token = generate_key(random.randint(1,100000))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    tree_name = models.CharField(max_length=100, choices=tree_choices)
    tree_planted_date = models.DateTimeField(auto_now_add=True)
    tree_pictures = models.ImageField(upload_to='media/treePlantedImages/ %Y/ %m/ %d/')
    tree_description = models.TextField(default=tree_name)
    points = models.PositiveIntegerField(default=0,verbose_name='points')
    
    
    def modify_points(self,new_points):
        self.points += new_points
        self.save()
        
    
    def __str__(self):
        return self.tree_description