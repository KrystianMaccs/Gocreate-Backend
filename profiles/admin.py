from django.contrib import admin
from .models import Artist



class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "gender", "phone_number", "city"]
    
    list_filter = ["gender", "country", "city"]
    
    list_display_links = ["id", "pkid", "user"]
    

admin.site.register(Artist, ArtistAdmin)