from django.shortcuts import render
from .models import Gallery
# Create your views here.

def gallery (requests):
   gallery = Gallery.objects.all()
   context = {
        'gallery' : gallery
    }

   return render(requests, 'gallery.html', context)
