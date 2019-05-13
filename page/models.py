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

class Organization(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    time = models.CharField(max_length=40, blank=True)
    subtitle1 = models.CharField(max_length=40, blank=True)
    content1 = models.TextField(blank=True)
    subtitle2 = models.CharField(max_length=40, blank=True)
    content2 = models.TextField(blank=True)
    location = models.CharField(max_length=40, blank=True)
    hyperlink = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.title

class Individual(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    time = models.CharField(max_length=40, blank=True)
    subtitle1 = models.CharField(max_length=40, blank=True)
    content1 = models.TextField(blank=True)
    subtitle2 = models.CharField(max_length=40, blank=True)
    content2 = models.TextField(blank=True)
    location = models.CharField(max_length=40, blank=True)
    hyperlink = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.title