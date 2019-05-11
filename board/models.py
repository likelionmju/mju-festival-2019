from django.db import models

class Board(models.Model):
    PURPOSE_CHOICES = (
        ('택시', '[택시]'),
        ('긴급', '[긴급]'),
        ('자유', '[자유]'),
    )

    title = models.CharField(max_length=50) 
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('publish')
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField() 
    password = models.CharField(max_length=20)
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default='자유')
    
    def __str__(self):
        return self.title