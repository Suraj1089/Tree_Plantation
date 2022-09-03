import email
from django.db import models

# Create your models here.

class ContactGrowGreen(models.Model):
    
    state_choices = (
        ('ANP','Andhra Pradesh'),
        ('ARU','Arunachal Pradesh'),
        ('ASS','Assam'),
        ('BIH','Bihar'),
        ('CHH','Chhattisgarh'),
        ('GOJ','Gujarat'),
        ('GOA','Goa'),
        ('HAR','Haryana'),
        ('HIM','Himachal Pradesh'),
        ('JHA','Jharkhand'),
        ('KAR','Karnataka'),
        ('KER','Kerala'),
        ('MAD','Madhya Pradesh'),
        ('MAH','Maharashtra'),
        ('MAN','Manipur'),
        ('MEG','Meghalaya'),
        ('MIZ','Mizoram'),
        ('NAG','Nagaland'),
        ('ODI','Odisha'),
        ('PUN','Punjab'),
        ('RAJ','Rajasthan'),
        ('TAM','Tamil Nadu'),
        ('UTT','Uttar Pradesh'),
        ('WES','West Bengal'),
        ('DEL','Delhi'),
        
        
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_state = models.CharField(max_length=5,choices=state_choices,default='India')
    user_message = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.first_name+' '+self.last_name