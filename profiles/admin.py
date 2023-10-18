from django.contrib import admin
from .models import Artist



class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "city"]
    
    list_filter = ["country", "city"]
    
    list_display_links = ["id", "pkid", "user"]
    

admin.site.register(Artist, ArtistAdmin)