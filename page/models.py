from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()
    menu = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    content = models.TextField()
    
    def __str__(self):
        return self.title