from django.contrib import admin
from .models import HomeContent,HomePageTrees
# Register your models here.

from django.utils.html import format_html

class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('slider_title','slider_images')
    search_fields = ('slider_title',)
    list_display_links = ('slider_title',)
    
    
    
class HomePageTreesAdmin(admin.ModelAdmin):
    list_display = ('tree_name','tree_image')
    search_fields = ('tree_name',)
    list_display_links = ('tree_name',)
    
    
admin.site.register(HomeContent,HomeContentAdmin)
admin.site.register(HomePageTrees,HomePageTreesAdmin)

#register model to backend (admin side)  