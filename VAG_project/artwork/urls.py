from django.urls import path
from . import views

urlpatterns = [
    path ('sculptures/', views.photography, name = 'sculptures'),
    path('photography/', views.photography, name='photography' ),
    path ('Paintings/', views.paintings ,  name= 'paintings'),
    path ('drawings/', views.drawings , name = 'drawings'),
    ]

