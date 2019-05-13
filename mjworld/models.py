from django.db import models

# Create your models here.
class Mjworld(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    tel = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    menu = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    takeout = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title