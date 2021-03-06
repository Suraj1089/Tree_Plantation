from django.contrib import admin

# Register plantree model in admin section

from .models import PlantaTree
from django.utils.html import format_html

class PlantaTreeAdmin(admin.ModelAdmin):
    #class to register the model in admin
   
    def myphoto(self,object):
        return format_html('<img src="{}"width="40"'.format(object.tree_pictures.url))
        
    list_display = ('username','tree_name','tree_planted_date','tree_pictures','tree_planted_date')
    search_field = ('username','tree_name','tree_planted_date','tree_planted_date')
    list_filter = ('tree_name',)
    list_display_links = ('username','tree_name')
    # list_editable = ('is_featured',)

admin.site.register(PlantaTree,PlantaTreeAdmin)