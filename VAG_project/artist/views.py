from django.shortcuts import render
from .models import Artist
# Create your views here.

def artist (requests):

  artist = Artist.objects.all()
  context = {
        'artist ' : artist
    }

  return render(requests, 'artist/artist.html', context)

