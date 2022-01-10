# Register your models here.
from django.contrib import admin
from .models import Gallery


# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo')
    List_display_links = ('id', 'title')
    list_per_page = 20