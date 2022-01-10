from django.db import models

# Create your models here.
class Gallery (models.Model):
    title = models.CharField(max_length= 250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)

    def __str__(self):
        return self.title