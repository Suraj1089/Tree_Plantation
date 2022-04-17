
from django.db import models

class PlantTree(models.Model):
    #class to plant tree    
    tree_choices = (
        ('N', 'Neem'),
        ('K','Karanja'),
        ('M','Mango'),
        ('J','Jamun'),
        ('B','Banyan'),
        ('A','Amrood'),
        ('BB','Bamboo'),
        ('BE','Ber'),
        ('NI','Nimboo'),
        
    )
    username = models.CharField(max_length=50,primary_key=True)
    tree_name = models.CharField(max_length=100, choices=tree_choices)
    tree_planted_date = models.DateTimeField(auto_now_add=True)
    tree_pictures = models.ImageField(upload_to='tree_planted_images/ %Y/ %m/ %d/')
    tree_description = models.TextField(default=tree_name)
    tree_planted_rewards = models.BigIntegerField()
    
    #method for incresing rewards of user
    def modify_tree_planted_rewards(self,tree_planted_rewards):
        self.tree_planted_rewards = tree_planted_rewards
        self.save()
        
    
    def __str__(self):
        return self.tree_description