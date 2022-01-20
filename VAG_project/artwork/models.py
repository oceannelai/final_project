from django.db import models

# Create your models here.

class Sculptures (models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Photography (models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Paintings (models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

class Drawings (models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title