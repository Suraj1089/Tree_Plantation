
from django import forms
from .models import ContactGrowGreen
from django.forms import ModelForm, TextInput, EmailInput

class ContactGrowGreenForm(forms.Form):
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
        
    first_name = forms.CharField(label='First Name',max_length=50)
    last_name = forms.CharField(label='Lat Name',max_length=50)
    email = forms.EmailField(label='Email')
    user_state = forms.ChoiceField(choices=state_choices)
    user_message = forms.CharField(label='Message',max_length=1000)
    
    