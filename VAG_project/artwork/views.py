from django.shortcuts import render
from .models import Photography,Paintings,Drawings, Sculptures
# Create your views here.

def sculptures (requests):
    sculptures = Sculptures.objects.all()
    context = {
        'sculptures' : sculptures
    }

    return render(requests, 'artwork/sculptures.html', context)

def photography (requests):
    photography = Photography.objects.all()
    context = {
        'photography' :photography
    }

    return render(requests, 'artwork/photography.html', context)


def paintings (requests):
    paintings = Paintings.objects.all()
    context = {
        'paintings' : paintings
    }
    return render(requests, 'artwork/Paintings.html', context)


def drawings (requests):
    drawings = Drawings.objects.all()
    context = {
        'drawings' : drawings
    }
    return render(requests, 'artwork/drawings.html', context)